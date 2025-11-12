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


@app.post("/generate")
async def generate_endpoint(
    request: Request,
    prompt: Optional[str] = Form(None),
):
    if prompt is None:
        try:
            payload = await request.json()
            prompt = payload.get("prompt")
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

    script_path = save_script(script_source, slug)

    try:
        video_path, duration = render_manim(script_path, slug, scene_name)
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    try:
        zip_path = make_export_zip(slug, script_path)
    except Exception as exc:  # pragma: no cover - best effort
        logger.warning("ZIP bundle failed: %s", exc)
        zip_path = None

    response = {
        "video_path": f"/media/{video_path.name}",
        "duration": duration,
        "code_path": f"/exports/{script_path.name}",
        "zip_path": f"/exports/{zip_path.name}" if zip_path else None,
        "source_code": script_source,
    }
    return response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
