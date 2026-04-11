import json
import logging
import os
import re
import shutil
import subprocess
import tempfile
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, ValidationError, validator

try:
    import google.generativeai as genai
except ImportError:  # pragma: no cover - optional dependency during tests
    genai = None


logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("econviz")

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
MEDIA_DIR = BASE_DIR / "media"
EXPORTS_DIR = BASE_DIR / "exports"

for directory in (STATIC_DIR, MEDIA_DIR, EXPORTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)


SUPPORTED_ACTIONS = {
    "SHOW_LINE",
    "MOVE_LINE",
    "ADD_LABEL",
    "HIGHLIGHT_EQUILIBRIUM",
    "SHOW_TEXT",
}


class Beat(BaseModel):
    t_start: float
    t_end: float
    action: str
    params: Dict[str, Any] = Field(default_factory=dict)
    narration: Optional[str] = None

    @validator("action")
    def validate_action(cls, value: str) -> str:
        if value not in SUPPORTED_ACTIONS:
            raise ValueError(f"Unsupported action: {value}")
        return value

    @validator("t_end")
    def validate_duration(cls, value: float, values: Dict[str, Any]) -> float:
        start = values.get("t_start", 0.0)
        if value <= start:
            raise ValueError("t_end must be greater than t_start")
        return value


app = FastAPI(title="EconViz Local")
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


FALLBACK_STORYBOARD: List[Dict[str, Any]] = [
    {
        "t_start": 0,
        "t_end": 3,
        "action": "SHOW_LINE",
        "params": {"name": "DEMAND"},
        "narration": "Baseline demand curve appears.",
    },
    {
        "t_start": 3,
        "t_end": 6,
        "action": "SHOW_LINE",
        "params": {"name": "SUPPLY"},
        "narration": "Supply enters to show equilibrium.",
    },
    {
        "t_start": 6,
        "t_end": 10,
        "action": "HIGHLIGHT_EQUILIBRIUM",
        "params": {},
        "narration": "Equilibrium point pulsates.",
    },
    {
        "t_start": 10,
        "t_end": 16,
        "action": "MOVE_LINE",
        "params": {"name": "DEMAND", "delta_shift": -1.2, "delta_slope": 0.0},
        "narration": "Demand shifts left to show a negative shock.",
    },
    {
        "t_start": 16,
        "t_end": 22,
        "action": "ADD_LABEL",
        "params": {"x": 3.0, "y": 7.5, "text": "Lower Q, lower P"},
        "narration": "Annotate the new equilibrium with lower price and quantity.",
    },
]


def slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    cleaned = "-".join(filter(None, cleaned.split("-")))
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return f"{cleaned[:40] or 'render'}-{timestamp}"


def parse_storyboard(raw: str) -> List[Dict[str, Any]]:
    def extract_json_block(text: str) -> str:
        fence = re.search(r"```(?:json)?\s*(\[[\s\S]*?\])\s*```", text, re.IGNORECASE)
        if fence:
            return fence.group(1)
        start = text.find("[")
        end = text.rfind("]")
        if start != -1 and end != -1 and end > start:
            return text[start : end + 1]
        return text

    raw = extract_json_block(raw.strip())
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Gemini returned invalid JSON: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError("Storyboard must be a JSON array.")
    beats = []
    for entry in data[:6]:
        try:
            beat = Beat(**entry)
        except ValidationError as exc:
            raise ValueError(f"Invalid beat: {exc}") from exc
        beats.append(beat.dict())
    total_duration = beats[-1]["t_end"] if beats else 0
    if total_duration > 120:
        raise ValueError("Storyboard exceeds 120 seconds.")
    return beats or FALLBACK_STORYBOARD


def gemini_storyboard(prompt: str) -> List[Dict[str, Any]]:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or genai is None:
        raise RuntimeError("GEMINI_API_KEY not configured or google-generativeai missing.")

    system_prompt = textwrap.dedent(
        """
        Act as a storyboard engine for short economics explainers (micro, macro, development, trade, etc.).
        Produce ONLY JSON: an array of up to 6 beats. No prose outside JSON.
        Fields per beat: t_start (seconds), t_end (seconds), action, params (object), narration (string).
        Allowed actions:
          - SHOW_LINE: params={{"name": "SUPPLY|DEMAND"}}
          - MOVE_LINE: params={{"name": "SUPPLY|DEMAND", "delta_slope": float, "delta_shift": float}}
          - ADD_LABEL: params={{"x": float, "y": float, "text": str}}
          - HIGHLIGHT_EQUILIBRIUM: params={{}}
          - SHOW_TEXT: params={{"text": str (<=240 chars), "position": "top_left|top_right|center|bottom_left|bottom_right"}}
        Use SHOW_TEXT to present concepts, comparisons, data, or narration for any economics topic.
        Keep total duration ≤ 120s, ≤ 6 beats. Ensure t_start increasing and t_end>t_start.
        """
    ).strip()

    genai.configure(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    model = genai.GenerativeModel(model_name=model_name)
    message = f"{system_prompt}\n\nUser prompt:\n{prompt}"
    response = model.generate_content(
        [{"role": "user", "parts": [{"text": message}]}],
        generation_config={"temperature": 0.4},
    )
    text = response.text if response else ""
    beats = parse_storyboard(text)
    logger.info("Generated storyboard with %d beats via Gemini.", len(beats))
    return beats


def save_storyboard(storyboard: List[Dict[str, Any]], slug: str) -> Path:
    json_path = MEDIA_DIR / f"{slug}.json"
    with json_path.open("w", encoding="utf-8") as fh:
        json.dump(storyboard, fh, indent=2)
    return json_path


def generate_repro_script(storyboard: List[Dict[str, Any]], slug: str) -> Path:
    script_path = EXPORTS_DIR / f"{slug}.py"
    beats_literal = json.dumps(storyboard, indent=2)
    script_lines = [
        '"""',
        "Auto-generated Manim scene for EconViz Local.",
        "",
        "Run:",
        f"    manim -pqh {slug}.py EconScene  # preview",
        f"    manim -p -r 1920,1080 -q h {slug}.py EconScene  # full quality",
        '"""',
        "from manim import *",
        "import numpy as np",
        "import textwrap",
        "",
        f"BEATS = {beats_literal}",
        "# To load beats from JSON instead:",
        "# import json",
        f"# with open('{slug}.json', 'r', encoding='utf-8') as fh:",
        "#     BEATS = json.load(fh)",
        "",
        "LABEL_POSITIONS = []",
        "TEXT_POSITIONS = {",
        "    'top_left': (1.2, 8.5),",
        "    'top_right': (8.8, 8.5),",
        "    'center': (5.0, 5.8),",
        "    'bottom_left': (1.5, 1.5),",
        "    'bottom_right': (8.5, 1.5),",
        "}",
        "",
        "def axes_with_labels():",
        "    axes = Axes(",
        "        x_range=[0, 10, 1],",
        "        y_range=[0, 10, 1],",
        "        x_length=9,",
        "        y_length=5,",
        '        axis_config={"include_tip": True},',
        "    )",
        '    x_label = Text("Quantity", font_size=40, color=BLACK).next_to(axes.x_axis, DOWN, buff=0.4)',
        '    y_label = Text("Price", font_size=40, color=BLACK).next_to(axes.y_axis, LEFT, buff=0.4)',
        "    labels = VGroup(x_label, y_label)",
        "    return axes, labels",
        "",
        "def build_line(axes, start, end, color):",
        "    return Line(axes.c2p(*start), axes.c2p(*end), color=color, stroke_width=6)",
        "",
        "def apply_move(line, axes, delta_slope=0.0, delta_shift=0.0):",
        "    start = axes.p2c(line.get_start())",
        "    end = axes.p2c(line.get_end())",
        "    base_dx = max(end[0] - start[0], 1e-3)",
        "    slope = (end[1] - start[1]) / base_dx",
        "    slope += delta_slope",
        "    new_start = (start[0], start[1] + delta_shift)",
        "    new_end = (end[0], new_start[1] + slope * base_dx)",
        "    return build_line(axes, new_start, new_end, line.color)",
        "",
        "def reserve_label_position(point):",
        "    for _ in range(3):",
        "        collision = False",
        "        for other in LABEL_POSITIONS:",
        "            if np.linalg.norm(other - point[:2]) < 0.6:",
        "                collision = True",
        "                point += np.array([0.2, 0.2, 0])",
        "                break",
        "        if not collision:",
        "            break",
        "    LABEL_POSITIONS.append(point[:2])",
        "    return point",
        "",
        "def add_label(scene, axes, text, x, y):",
        "    txt = Text(text, font_size=36, color=BLACK)",
        "    bg = SurroundingRectangle(txt, color=GRAY, buff=0.15, fill_opacity=0.05)",
        "    group = VGroup(bg, txt)",
        "    target = reserve_label_position(np.array(axes.c2p(x, y)))",
        "    group.move_to(target)",
        "    scene.play(FadeIn(group, shift=UP * 0.2), run_time=0.8)",
        "",
        "def add_text_block(scene, axes, text, position):",
        "    wrapped = textwrap.fill(text, width=48)",
        "    lines = wrapped.split('\\n') if wrapped else ['Economics']",
        "    paragraph = Paragraph(*lines, alignment='left', line_spacing=0.8, font_size=34, color=BLACK)",
        "    anchor = TEXT_POSITIONS.get(position, TEXT_POSITIONS['center'])",
        "    paragraph.move_to(axes.c2p(*anchor))",
        "    panel = SurroundingRectangle(paragraph, color=GRAY, buff=0.3, fill_opacity=0.05)",
        "    block = VGroup(panel, paragraph)",
        "    scene.play(FadeIn(block, shift=UP * 0.15), run_time=1.0)",
        "",
        "def highlight_equilibrium(scene, axes):",
        "    eq_point = axes.c2p(5, 5)",
        "    dot = Dot(eq_point, color=YELLOW, radius=0.08)",
        "    dashed_h = DashedLine(axes.c2p(0, 5), axes.c2p(10, 5), color=YELLOW_D)",
        "    dashed_v = DashedLine(axes.c2p(5, 0), axes.c2p(5, 10), color=YELLOW_D)",
        "    scene.play(FadeIn(dot), Create(dashed_h), Create(dashed_v), run_time=1.2)",
        "    scene.play(Indicate(dot), run_time=1.0)",
        "",
        "class EconScene(Scene):",
        "    def construct(self):",
        "        config.frame_rate = 30",
        "        config.pixel_width = 1920",
        "        config.pixel_height = 1080",
        "        config.background_color = WHITE",
        "        axes, labels = axes_with_labels()",
        "        self.play(Create(axes), FadeIn(labels), run_time=1.5)",
        "        supply = build_line(axes, (0, 1), (10, 9), BLUE)",
        "        demand = build_line(axes, (0, 9), (10, 1), RED)",
        '        lines = {"SUPPLY": supply, "DEMAND": demand}',
        "",
        "        for beat in BEATS:",
        '            duration = max(0.2, beat["t_end"] - beat["t_start"])',
        '            action = beat["action"]',
        '            params = beat.get("params", {})',
        '            if action == "SHOW_LINE":',
        '                line_name = params.get("name", "").upper()',
        "                line = lines.get(line_name)",
        "                if line:",
        "                    self.play(Create(line), run_time=duration)",
        '            elif action == "MOVE_LINE":',
        '                line_name = params.get("name", "").upper()',
        "                line = lines.get(line_name)",
        "                if line:",
        "                    updated = apply_move(",
        "                        line,",
        "                        axes,",
        '                        delta_slope=params.get("delta_slope", 0.0),',
        '                        delta_shift=params.get("delta_shift", 0.0),',
        "                    )",
        "                    self.play(Transform(line, updated), run_time=duration)",
        '            elif action == "ADD_LABEL":',
        "                add_label(",
        "                    self,",
        "                    axes,",
        '                    params.get("text", "Label"),',
        '                    params.get("x", 5.0),',
        '                    params.get("y", 5.0),',
        "                )",
        '            elif action == "HIGHLIGHT_EQUILIBRIUM":',
        "                highlight_equilibrium(self, axes)",
        '            elif action == "SHOW_TEXT":',
        "                add_text_block(",
        "                    self,",
        "                    axes,",
        '                    params.get("text", "Economics insight"),',
        '                    params.get("position", "center"),',
        "                )",
        "            self.wait(0.1)",
    ]
    script_body = "\n".join(script_lines) + "\n"
    with script_path.open("w", encoding="utf-8") as fh:
        fh.write(script_body)
    logger.info("Exported reproduction script to %s", script_path)
    return script_path


def render_manim(script_path: Path, slug: str, storyboard: List[Dict[str, Any]]) -> Tuple[Path, float]:
    tmp_media_dir = Path(tempfile.mkdtemp(prefix="manim_media_"))
    video_stub = MEDIA_DIR / f"{slug}_video.mp4"
    cmd = [
        "manim",
        str(script_path),
        "EconScene",
        "-q",
        "h",
        "-r",
        "1920,1080",
        "--disable_caching",
        "--media_dir",
        str(tmp_media_dir),
        "-o",
        slug,
    ]
    logger.info("Running Manim render: %s", " ".join(cmd))
    try:
        process = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise RuntimeError("Manim CLI not found. Install manim to render scenes.") from exc
    if process.returncode != 0:
        logger.error("Manim render failed: %s", process.stderr)
        raise RuntimeError("Manim render failed. See logs for details.")
    mp4_candidates = sorted(tmp_media_dir.rglob("*.mp4"), key=lambda p: p.stat().st_mtime)
    if not mp4_candidates:
        raise RuntimeError("No MP4 file produced by Manim.")
    if video_stub.exists():
        video_stub.unlink()
    shutil.move(str(mp4_candidates[-1]), video_stub)
    shutil.rmtree(tmp_media_dir, ignore_errors=True)
    duration = max((beat["t_end"] for beat in storyboard), default=0.0)
    return video_stub, float(duration)


def tts_elevenlabs(storyboard: List[Dict[str, Any]], slug: str) -> Optional[Path]:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        return None
    voice_id = os.getenv("VOICE_ID", "Rachel")
    narrations = [beat.get("narration", "") for beat in storyboard if beat.get("narration")]
    if not narrations:
        return None
    payload = {"text": "\n".join(narrations), "model_id": "eleven_multilingual_v2"}
    headers = {"xi-api-key": api_key, "accept": "audio/mpeg"}
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    logger.info("Requesting ElevenLabs TTS for %d narration segments.", len(narrations))
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
    except requests.RequestException as exc:
        logger.error("ElevenLabs request error: %s", exc)
        return None
    if response.status_code != 200:
        logger.error("ElevenLabs request failed: %s - %s", response.status_code, response.text)
        return None
    wav_path = MEDIA_DIR / f"{slug}.mp3"
    with wav_path.open("wb") as fh:
        fh.write(response.content)
    return wav_path


def mux_ffmpeg(video_path: Path, audio_path: Path, slug: str) -> Path:
    output_path = MEDIA_DIR / f"{slug}.mp4"
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(video_path),
        "-i",
        str(audio_path),
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        str(output_path),
    ]
    logger.info("Muxing audio via ffmpeg.")
    try:
        process = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise RuntimeError("FFmpeg not found. Install ffmpeg to enable audio muxing.") from exc
    if process.returncode != 0:
        logger.error("ffmpeg mux failed: %s", process.stderr)
        raise RuntimeError("FFmpeg mux failed.")
    return output_path


def make_export_zip(slug: str, script_path: Path, json_path: Path) -> Path:
    import zipfile

    zip_path = EXPORTS_DIR / f"{slug}.zip"
    readme = textwrap.dedent(
        f"""\
        EconViz Local export bundle for {slug}

        Contents:
        - {slug}.py : Manim script
        - {slug}.json : Storyboard beats

        Run:
            manim -p -r 1920,1080 -q h {slug}.py EconScene
        """
    )
    with zipfile.ZipFile(zip_path, "w") as bundle:
        bundle.write(script_path, arcname=f"{slug}.py")
        bundle.write(json_path, arcname=f"{slug}.json")
        bundle.writestr("README.txt", readme)
    return zip_path


def finalize_video_path(video_stub: Path, slug: str) -> Path:
    final_path = MEDIA_DIR / f"{slug}.mp4"
    if final_path.exists():
        final_path.unlink()
    shutil.move(video_stub, final_path)
    return final_path


@app.get("/", response_class=HTMLResponse)
async def serve_index() -> HTMLResponse:
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="UI not found.")
    return HTMLResponse(index_path.read_text(encoding="utf-8"))


@app.get("/exports/{filename}")
async def download_export(filename: str):
    file_path = EXPORTS_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Export not found.")
    headers = {"Content-Disposition": f'attachment; filename="{file_path.name}"'}
    return FileResponse(file_path, media_type="application/octet-stream", headers=headers)


@app.post("/generate")
async def generate_endpoint(
    request: Request,
    prompt: Optional[str] = Form(None),
    use_tts: bool = Form(False),
):
    if prompt is None:
        try:
            payload = await request.json()
            prompt = payload.get("prompt")
            use_tts = payload.get("use_tts", False)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid payload.")
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")

    slug = slugify(prompt)
    try:
        storyboard = gemini_storyboard(prompt)
    except (RuntimeError, ValueError) as exc:
        logger.error("Storyboard generation failed: %s", exc)
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    json_path = save_storyboard(storyboard, slug)
    script_path = generate_repro_script(storyboard, slug)

    try:
        video_stub, duration = render_manim(script_path, slug, storyboard)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    audio_track = None
    final_video = video_stub
    if use_tts:
        audio_track = tts_elevenlabs(storyboard, slug)
        if audio_track:
            try:
                final_video = mux_ffmpeg(video_stub, audio_track, slug)
                if audio_track.exists():
                    audio_track.unlink()
                if video_stub.exists():
                    video_stub.unlink()
            except RuntimeError:
                logger.warning("Falling back to silent video after FFmpeg failure.")
                final_video = finalize_video_path(video_stub, slug)
        else:
            final_video = finalize_video_path(video_stub, slug)
    else:
        final_video = finalize_video_path(video_stub, slug)

    try:
        zip_path = make_export_zip(slug, script_path, json_path)
    except Exception as exc:
        logger.warning("ZIP bundle failed: %s", exc)
        zip_path = None

    response = {
        "video_path": f"/media/{final_video.name}",
        "duration": duration,
        "storyboard": storyboard,
        "code_path": f"/exports/{script_path.name}",
        "zip_path": f"/exports/{zip_path.name}" if zip_path else None,
    }
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
