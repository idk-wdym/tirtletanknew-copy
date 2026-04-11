# Code2Video Local

**Code2Video** is an AI-powered tool that turns any topic into an animated explainer video. Type in a concept — like "explain the Pythagorean theorem" or "visualize supply and demand" — and it automatically generates a fully rendered 1080p animation with optional voiceover narration. No animation skills required.

Turn any idea into a rendered Manim animation video — powered by Gemini and optionally narrated by ElevenLabs.

Type a concept (e.g. "explain price equilibrium"), and the app generates a Manim Python script, renders it at 1080p, and lets you download the video. Optionally, it synthesizes a voiceover with ElevenLabs and muxes it in via FFmpeg.

---

## Prerequisites

- Python 3.11
- [Manim](https://docs.manim.community/en/stable/installation.html) (`pip install manim` requires additional system deps — see Manim docs)
- FFmpeg (for audio muxing; optional)
- Your own **Gemini API key** (from [Google AI Studio](https://aistudio.google.com/))
- Your own **ElevenLabs API key** (optional, for TTS narration)

---

## Setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Configuration

Export your API keys before launching. You need to supply your own keys — the app does not include any.

```bash
# Required — get yours at https://aistudio.google.com/
export GEMINI_API_KEY=your_gemini_key_here

# Optional — get yours at https://elevenlabs.io/
export ELEVENLABS_API_KEY=your_elevenlabs_key_here

# Optional — ElevenLabs voice ID (defaults to Rachel)
export VOICE_ID=Rachel
```

### Optional environment variables

| Variable | Default | Description |
|---|---|---|
| `GEMINI_API_KEY` | *(required)* | Your Gemini API key |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Gemini model to use for script generation |
| `ELEVENLABS_API_KEY` | *(none)* | ElevenLabs key; omit to skip TTS |
| `ELEVENLABS_MODEL` | `eleven_multilingual_v2` | ElevenLabs TTS model |
| `VOICE_ID` | `Rachel` | ElevenLabs voice ID |
| `VIDEO_SCENE_NAME` | `GeneratedScene` | Manim scene class name |
| `VIDEO_SYSTEM_PROMPT` | *(built-in)* | Override the LLM system prompt |

---

## Running

```bash
uvicorn app:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Usage

1. Enter a topic or concept in the text box (e.g. "explain covalent bonds" or "visualize supply and demand").
2. Optionally check **Use ElevenLabs TTS** to add a voiceover (requires `ELEVENLABS_API_KEY`).
3. Click **Generate script & video** and wait up to ~90 seconds.
4. Download the rendered `.mp4`, the generated `.py` Manim script, a `.zip` export bundle, or the `.mp3` audio separately.

---

## Project Structure

```
.
├── app.py              # FastAPI backend — LLM generation, Manim render, TTS, muxing
├── requirements.txt    # Python dependencies
├── static/
│   ├── index.html      # Frontend UI
│   └── styles.css      # Styles
├── media/              # Rendered MP4s and audio files (auto-created)
└── exports/            # Generated Manim scripts and ZIP bundles (auto-created)
```

---

## How It Works

1. **Prompt → Script**: Your prompt is sent to Gemini, which returns a complete Manim Python script.
2. **Script → Video**: The script is saved to `exports/` and rendered with the `manim` CLI at 1920×1080 / 30 FPS.
3. **TTS (optional)**: If enabled, the prompt text is sent to ElevenLabs to generate an MP3 narration.
4. **Muxing (optional)**: FFmpeg combines the silent video and the audio track into a final MP4.
5. **Download**: All outputs are served directly from the app.

---

## Notes

- Render time depends on animation complexity — budget 30–90 seconds per video.
- FFmpeg must be installed system-wide for audio muxing to work.
- Manim has its own system-level dependencies (LaTeX, Cairo, etc.). Follow the [Manim installation guide](https://docs.manim.community/en/stable/installation.html) for your OS before running this project.
