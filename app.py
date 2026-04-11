import logging
import os
import re
import shutil
import subprocess
import tempfile
import textwrap
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

import requests
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

try:  # pragma: no cover - optional dependency for hosted LLMs
    import google.generativeai as genai
except ImportError:  # pragma: no cover - optional during tests
    genai = None


logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("videoviz")

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
MEDIA_DIR = BASE_DIR / "media"
EXPORTS_DIR = BASE_DIR / "exports"

for directory in (STATIC_DIR, MEDIA_DIR, EXPORTS_DIR):
    directory.mkdir(parents=True, exist_ok=True)


app = FastAPI(title="Code2Video Local")
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    cleaned = "-".join(filter(None, cleaned.split("-")))
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return f"{cleaned[:40] or 'render'}-{timestamp}"


def extract_code_block(raw: str) -> str:
    """Return the first fenced code block or the raw text if no fences exist."""

    match = re.search(r"```(?:python)?\s*([\s\S]+?)```", raw, flags=re.IGNORECASE)
    code = match.group(1) if match else raw
    code = code.strip()
    if not code:
        raise ValueError("LLM returned empty code block.")
    return code


def ensure_scene_present(source: str, scene_name: str) -> None:
    pattern = rf"class\s+{re.escape(scene_name)}\s*\("
    if not re.search(pattern, source):
        raise ValueError(
            f"Generated script must define a Scene subclass named {scene_name}."
        )


def patch_dash_length_usage(source: str) -> str:
    if "dash_length" not in source:
        return source
    sentinel = "# Code2Video dash_length patch"
    if sentinel in source:
        return source

    injection = textwrap.dedent(
        f"""
        {sentinel}
        from manim import Line as _CODE2VIDEO_ORIGINAL_LINE, DashedLine as _CODE2VIDEO_DASHED_LINE

        def Line(*args, dash_length=None, **kwargs):
            if dash_length is not None:
                return _CODE2VIDEO_DASHED_LINE(*args, dash_length=dash_length, **kwargs)
            return _CODE2VIDEO_ORIGINAL_LINE(*args, **kwargs)
        """
    ).strip()

    lines = source.splitlines()
    insert_idx = 0
    for idx, line in enumerate(lines):
        if line.lstrip().startswith("from manim import"):
            insert_idx = idx + 1
    lines.insert(insert_idx, injection)
    return "\n".join(lines)


def get_scene_name() -> str:
    return os.getenv("VIDEO_SCENE_NAME", "GeneratedScene")


def build_system_prompt(scene_name: str) -> str:
    custom_prompt = os.getenv("VIDEO_SYSTEM_PROMPT")
    if custom_prompt:
        return custom_prompt.strip()

    return textwrap.dedent(
        f"""
        You are an assistant that writes complete Manim scripts.
        Requirements:
        - Output ONLY Python code with necessary imports.
        - Define a scene class named {scene_name} that subclasses Scene (or a Manim variant).
        - Configure 1920x1080 resolution at 30 FPS and a white background if needed.
        - Keep the script self-contained with deterministic geometry/text.
        - Do not reference external files, network calls, or environment variables.
        - Feel free to design layouts, timelines, and animations for any topic requested.
        - Comment sparingly to clarify complex animation blocks.
Generated script must define a Scene subclass named GeneratedScene
Generated script must define a Scene subclass named GeneratedScene
Generated script must define a Scene subclass named GeneratedScene
Generated script must define a Scene subclass named GeneratedScene
Generated script must define a Scene subclass named GeneratedScene
        Strict API rules (prevent TypeErrors):
        - If you need dashed geometry, call DashedLine or Line().set_stroke(dash_array=...). Do NOT pass `dash_length` directly to Line; if you want to hint at dashed behavior, mention the helper.
        - Use Text or Paragraph for labels. Never pass `wrap_width` to Text/MarkupText; wrap manually before constructing the mobject.
        - `x_range`/`y_range` only belong on Axes construction or when plotting with axes.plot/axes.get_graph. Do NOT pass them to helper methods like get_horizontal_line, get_vertical_line, Line, or Dot.
        - Prefer axes.plot over the deprecated axes.get_graph.
        - Use MathTex sparingly and only when LaTeX is essential.
        - Provide all required imports explicitly (from manim import ...).
        - Please avoid x_unit_size and y_unit_size
    Generate Manim code for the animation that follows these standards:
    - Use the Manim library to write code that defines each scene, the graphical elements, and their transformations. The overall animation should e xplain and visualize the concepts of the content that the user has inputted, which is at the end of this prompt.
    - For this video, generate 2-3 examples that comprehensively visualize and explain the concepts which the user wishes to learn.
    - All of the Manim code has to be in Python with proper syntax with no errors at all.
    - Do not include Markdown Code Block Syntax, using straight raw code only. Do not include "'''" or "*"'python" in any location.
    - DO NOT EXPLAIN YOUR CODE GENERATION. STRICTLY PROVIDE CODE AND CODE ONLY.
    - The class that you use for the Manim generation should STRICTLY be called "RequestGeneration" and nothing else.
    - You must use latex to write out all text content.
    5. Optimize the Manim code for accessibility and comprehension:
    - Refine the code to ensure that it represents the educational content in the most visually engaging and intuitive manner possible.
    - Keep the target audience in mind and adapt the code to suit the needs of visual learners.
    - The code must ensure that ALL text content has padding from the borders of the sgreen. Text can be aligned appropriately based on the animatio n, but should never go off screen or be right on the edge of the screen.
    - The text can use different font sizes, but only if you deem it to be appropriate. For example, you can make the text size for the main concept slightly larger than the text size for the examples. Formatting such as bold, italics, or underline can be used appropriately based on the given c ontent.
    - You should clear the screen of previous content if you need more space.
    - The code must make the transition between animations and visual elements as smooth as possible.
    - The code that adds some color for visual separation to the text and animations that explain the process.
    - Make sure the colors you apply to the text are legible. Make sure you have good color contrast for text legibility. You have to use all of the colors appropriately and in ways that make the animation and concepts clearer for the user. Follow the standards of the Web Content Accessibility
    Guidelines (WCAG) 2.
    6. Output the Manim code:
    - Return the completed code as an output that meets all the above standards and contains no errors.
    7. If you run into an error, we will tell you and you will regenerate the code based on that specification.
    As a reminder, your goal is to enable the efficient creation of high-quality animations that help students, educators, and lifelong learners grasp complex concepts through visually appealing, easy-to-understand representations.
    If you create a graph of any frame (which is preferred), make sure you CLEAR the frame before and after the render of the entire graph and all its
    components.
    Remember, you MUST clear the screen if it is full after ANY generations. Make sure ALL NEW CONTENT IS ON NEW LINES. NO OVERLAPS CAN BE MADE. MAKE S URE THESE VIDEOS ARE SIZABLY LONG AND HAVE GOOD CONTENT.
    If an equation is especially long, please render it onto multiple lines so that it doesn't go outside of the screen's viewport.
    Please ensure that there is visual seperation between all text elements.
    ALWAYS ALWAYS ALWAYSalways names the scene GeneratedScene (case-sensitive










        """
    ).strip()


def gemini_generate_script(prompt: str, scene_name: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or genai is None:
        raise RuntimeError("GEMINI_API_KEY not configured or google-generativeai missing.")

    system_prompt = build_system_prompt(scene_name)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name=model_name)
    message = textwrap.dedent(
        f"""
        {system_prompt}

        User prompt:
        {prompt}
        """
    ).strip()
    response = model.generate_content(
        [{"role": "user", "parts": [{"text": message}]}],
        generation_config={"temperature": 0.2},
    )
    text = response.text if response else ""
    code = extract_code_block(text)
    ensure_scene_present(code, scene_name)
    logger.info("Generated script via Gemini (%s).", model_name)
    return code


def generate_script(prompt: str, scene_name: str) -> str:
    provider = os.getenv("VIDEO_LLM_PROVIDER", "gemini").lower()
    if provider == "gemini":
        return gemini_generate_script(prompt, scene_name)
    raise RuntimeError(f"Unsupported LLM provider: {provider}")


def save_script(source: str, slug: str) -> Path:
    script_path = EXPORTS_DIR / f"{slug}.py"
    with script_path.open("w", encoding="utf-8") as fh:
        fh.write(source)
    return script_path


def probe_video_duration(video_path: Path) -> Optional[float]:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=duration",
        "-of",
        "default=nw=1:nk=1",
        str(video_path),
    ]
    try:
        process = subprocess.run(
            cmd, capture_output=True, text=True, timeout=10, check=True
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        logger.warning("ffprobe unavailable; duration omitted for %s", video_path.name)
        return None
    output = process.stdout.strip()
    try:
        return float(output)
    except ValueError:
        logger.warning("Unable to parse duration from ffprobe output: %s", output)
        return None


def render_manim(script_path: Path, slug: str, scene_name: str) -> Tuple[Path, float]:
    tmp_media_dir = Path(tempfile.mkdtemp(prefix="manim_media_"))
    final_video = MEDIA_DIR / f"{slug}.mp4"
    cmd = [
        "manim",
        str(script_path),
        scene_name,
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

    if final_video.exists():
        final_video.unlink()
    shutil.move(str(mp4_candidates[-1]), final_video)
    shutil.rmtree(tmp_media_dir, ignore_errors=True)
    duration = probe_video_duration(final_video) or 0.0
    return final_video, duration


def make_export_zip(slug: str, script_path: Path) -> Path:
    import zipfile

    zip_path = EXPORTS_DIR / f"{slug}.zip"
    readme = textwrap.dedent(
        f"""\
        Code2Video export bundle for {slug}

        Contents:
        - {slug}.py : Generated Manim script

        Render locally:
            manim -p -r 1920,1080 -q h {slug}.py {get_scene_name()}
        """
    )
    with zipfile.ZipFile(zip_path, "w") as bundle:
        bundle.write(script_path, arcname=f"{slug}.py")
        bundle.writestr("README.txt", readme)
    return zip_path


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


def synthesize_tts(text: str, slug: str) -> Optional[Path]:
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        return None
    payload = {
        "text": text.strip(),
        "model_id": os.getenv("ELEVENLABS_MODEL", "eleven_multilingual_v2"),
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5},
    }
    if not payload["text"]:
        return None
    voice_id = os.getenv("VOICE_ID", "Rachel")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key, "accept": "audio/mpeg"}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
    except requests.RequestException as exc:  # pragma: no cover - network
        logger.error("ElevenLabs request error: %s", exc)
        return None
    if response.status_code != 200:
        logger.error("ElevenLabs request failed: %s - %s", response.status_code, response.text)
        return None
    audio_path = MEDIA_DIR / f"{slug}.mp3"
    with audio_path.open("wb") as fh:
        fh.write(response.content)
    return audio_path


def mux_ffmpeg(video_path: Path, audio_path: Path, slug: str) -> Path:
    output_path = MEDIA_DIR / f"{slug}_with_audio.mp4"
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
    logger.info("Muxing audio via ffmpeg for %s", slug)
    try:
        process = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError as exc:
        raise RuntimeError("FFmpeg not found. Install ffmpeg to enable audio muxing.") from exc
    if process.returncode != 0:
        logger.error("FFmpeg mux failed: %s", process.stderr)
        raise RuntimeError("FFmpeg mux failed.")
    return output_path


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
            use_tts = bool(payload.get("use_tts", False))
        except Exception as exc:  # includes JSON decode errors
            raise HTTPException(status_code=400, detail="Invalid payload.") from exc

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required.")

    slug = slugify(prompt)
    scene_name = get_scene_name()
    try:
        script_source = generate_script(prompt, scene_name)
    except RuntimeError as exc:
        logger.error("Script generation failed: %s", exc)
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    script_source = patch_dash_length_usage(script_source)
    script_path = save_script(script_source, slug)

    try:
        video_path, duration = render_manim(script_path, slug, scene_name)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    final_video = video_path
    audio_track = None
    if use_tts:
        audio_text = prompt or ""
        audio_track = synthesize_tts(audio_text, slug)
        if audio_track:
            try:
                silent_video = video_path
                final_video = mux_ffmpeg(video_path, audio_track, slug)
                video_path = final_video
                if silent_video.exists() and silent_video != final_video:
                    silent_video.unlink(missing_ok=True)
            except RuntimeError as exc:
                logger.warning("Falling back to silent video after FFmpeg failure: %s", exc)
                final_video = video_path
        else:
            logger.warning("TTS requested but no audio generated; returning silent video.")

    try:
        zip_path = make_export_zip(slug, script_path)
    except Exception as exc:  # pragma: no cover - best effort
        logger.warning("ZIP bundle failed: %s", exc)
        zip_path = None

    response = {
        "video_path": f"/media/{final_video.name}",
        "duration": duration,
        "code_path": f"/exports/{script_path.name}",
        "zip_path": f"/exports/{zip_path.name}" if zip_path else None,
        "source_code": script_source,
        "audio_path": f"/media/{audio_track.name}" if audio_track else None,
    }
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
