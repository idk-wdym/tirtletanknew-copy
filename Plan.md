# EconViz Local — Plan.md (PRD, v1.1)

Minimal local project that turns an economics prompt into a ≤2‑min 1080p30 video via Manim, with Gemini storyboard and optional ElevenLabs TTS — now also emits a self-contained Manim render script you can download and rerun.

---

## 0) One-paragraph summary

Build a tiny, single-user local app that accepts an economics prompt, asks Gemini for a compact, time-coded storyboard (≤6 beats) in a tiny DSL, renders a Manim scene (axes + S/D lines + labels + equilibrium) to 1920×1080@30fps MP4, optionally synthesizes TTS with ElevenLabs, muxes with FFmpeg, and saves both `./media/<slug>.mp4` and `./media/<slug>.json`.  
New: The app also generates a single-file Manim script (e.g., `./exports/<slug>.py`) that reproduces the exact video from the saved storyboard, plus an optional ZIP bundle for convenience. The HTML page links to the MP4 and the code artifact(s). Everything runs locally on macOS, no DB/Redis/Celery/frameworks.

---

## 1) Goals & Non-Negotiables

Primary goal: Local generation of short economics explainer videos with accurate on-screen labeling and coarse A/V sync.

Non-negotiables (unchanged + new):
- 1080p30 output, ≤120s.
- Tools: manim, ffmpeg, uvicorn (local).
- Tiny project (see §4).
- Collision-aware labels; S/D; equilibrium with dashed helpers.
- Save `./media/<slug>.mp4` and `./media/<slug>.json`.
- New: Also save `./exports/<slug>.py` (self-contained Manim script). Optional `./exports/<slug>.zip` (contains `.py`, `.json`, and a small README snippet). UI exposes download links.

---

## 2) Scope

In: Prompt → storyboard (Gemini) → render (Manim) → optional TTS (ElevenLabs) → mux (FFmpeg) → store media+JSON → emit reproducible code file → minimal UI with links.  
Out: Auth, multi-tenant, queues, fancy UI.

---

## 3) Environments & Keys

- `GEMINI_API_KEY` (required)
- `ELEVENLABS_API_KEY` (optional)
- `VOICE_ID` (optional, default “Rachel”)

Platform: macOS (Apple Silicon), Python 3.10+.

---

## 4) Minimal File Layout

```
.
├── app.py                      # FastAPI + Gemini + Manim + TTS + FFmpeg + code export
├── requirements.txt
├── static/
│   ├── index.html              # single page; inline <script>
│   └── styles.css              # small
├── media/                      # outputs (.mp4, .json, .wav temp)
└── exports/                    # NEW: downloadable artifacts (<slug>.py, <slug>.zip)
```

We still keep source files minimal. Exports are generated artifacts created per render.

---

## 5) Functional Requirements

### 5.1 User Flow
1. Visit `http://127.0.0.1:8000/`.
2. Form: `<textarea prompt>` (prefilled “Explain a negative demand shock”), checkbox `use_tts`.
3. Submit → `POST /generate` (form or JSON).
4. Backend:
   - Gemini → storyboard (≤6 beats) or fallback.
   - Manim → `./media/<slug>_video.mp4`.
   - Optional TTS → WAV; adjust beat waits; FFmpeg mux → `./media/<slug>.mp4`.
   - Persist `./media/<slug>.json`.
   - NEW: Generate `./exports/<slug>.py` (self-contained Manim Scene that reads the JSON or embeds the beats).
   - Optionally package `./exports/<slug>.zip` containing:
     - `<slug>.py`
     - `<slug>.json` (storyboard)
     - `README.txt` (how to run `manim -pqh <slug>.py EconScene`)
5. Response JSON includes `video_path`, `duration`, `storyboard`, `code_path`, and `zip_path` if created.
6. UI shows links to MP4 and code download(s).

### 5.2 Endpoints
- `GET /` → `static/index.html`.
- `POST /generate` → orchestrates; returns:

```json
{
  "video_path": "/media/<slug>.mp4",
  "duration": 71.3,
  "storyboard": [ ... ],
  "code_path": "/exports/<slug>.py",
  "zip_path": "/exports/<slug>.zip"
}
```

- `GET /media/{filename}` → serve from `./media`.
- NEW: `GET /exports/{filename}` → serve from `./exports`.

---

## 6) Storyboard Contract (same DSL, strict JSON)

- System prompt to Gemini yields pure JSON array of beats, ≤6 beats, ≤120s total.
- Fallback storyboard exists for negative demand shock.
- DSL: `SHOW_LINE`, `MOVE_LINE(name, delta_slope, delta_shift)`, `ADD_LABEL(x,y,text)`, `HIGHLIGHT_EQUILIBRIUM()`.

---

## 7) Geometry, Rendering & Timing

(unchanged) — Axes 0..10, D: (0,9)->(10,1), S: (0,1)->(10,9), E≈(5,5), deterministic seed, anti-overlap nudging (0.2,0.2) up to 3 times, waits from `t_end - t_start`. With TTS, stretch waits to narration durations (±50 ms target).

---

## 8) Backend Design

### 8.1 Responsibilities (additions in bold)
- `gemini_storyboard(prompt)` -> `list[Beat]` with strict validation/fallback.
- `render_manim(storyboard, out_slug)` -> `(video_path, duration_s)`.
- `tts_elevenlabs(segments, out_slug)` -> `audio_wav | None`.
- `mux_ffmpeg(video_mp4, audio_wav, out_mp4)`.
- `generate_repro_script(storyboard, out_slug)` -> `code_py_path`.
  - Emits a single runnable Manim script (`<slug>.py`) that:
    - Defines one Scene reproducing axes/S/D/equilibrium and the same beats.
    - Either embeds the beats inline or loads `../media/<slug>.json` if present (prefer embedding for portability).
    - Uses the same 1080p30 config and deterministic seed.
    - Includes minimal anti-overlap helper.
    - Top-of-file comment shows quick run instructions, e.g.:
      ```
      # manim -pqh <slug>.py EconScene (for quick)
      # manim -p -r 1920,1080 -q h <slug>.py EconScene (1080p high quality)
      ```
- `make_export_zip(out_slug, paths...)` -> `zip_path` (optional).
- Routes: `GET /`, `POST /generate`, `GET /media/*`, `GET /exports/*`.
- `__main__` → uvicorn on `127.0.0.1:8000`.

### 8.2 Data Model

Beat unchanged; validation unchanged.

### 8.3 Error Handling & Fallbacks

- If code export fails, continue; return video with a warning and omit `code_path`/`zip_path`.
- ZIP creation optional; if FFmpeg missing → return video-only path (the `_video.mp4`) and still export code.

---

## 9) Frontend (HTML + CSS)

`static/index.html` updates:
- After success, render:
  - “🎬 Download video” → link to `/media/<slug>.mp4`
  - “📄 Download code (.py)” → link to `/exports/<slug>.py`
  - “🗜️ Download bundle (.zip)” → link to `/exports/<slug>.zip` (if present)
- A small `<details>` block to preview returned JSON beats (optional).

CSS remains small and simple.

---

## 10) Performance & UX

- Still target ≤90s generation on M-series for default scene.
- Code export is instantaneous (string write + optional zip).

---

## 11) Security & Privacy

- Local bind `127.0.0.1`.
- Sanitize filenames from prompts (slugify).
- Set `Content-Disposition: attachment` for `/exports/*` responses.

---

## 12) Logging & Cleanup

- Log code export path(s).
- Keep `.py` and `.json` for reproducibility.
- Optionally delete `.wav` post-mux; ZIP is small.

---

## 13) Risks & Mitigations

- Mismatch between runtime scene and export script → Use the same helper functions/constants in both paths (script is generated from the same in-memory logic); include a short self-test (count beats).
- Font/layout drift across machines → Deterministic seed + conservative font size; note that font availability can vary.

---

## 14) Acceptance Criteria (updated)

Running:

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

- Visit `/`, click Generate → within ~90s:
  - MP4 in `./media/` (1080p30).
  - JSON in `./media/`.
  - `.py` script in `./exports/` that re-renders the same sequence when run with Manim.
  - (Optional) `.zip` bundle in `./exports/`.
  - UI shows links to MP4 and code download(s).
  - Labels avoid overlap (or nudge), equilibrium highlighted, TTS (if enabled) roughly aligned.

---

## 15) Dependencies (unchanged)

```
fastapi
uvicorn
google-generativeai
manim
pydantic
python-multipart
requests
```

External: ffmpeg installed; Manim OK on macOS (Apple Silicon).

---

## 16) Test Plan (manual) — add code export checks

1. Code export exists: After generation, download `<slug>.py`; run:

```
manim -p -r 1920,1080 -q h exports/<slug>.py EconScene
```

→ Produces a visually matching render (minor timing differences acceptable).

2. ZIP bundle: Download and unzip; render from inside folder; succeed.

3. Missing JSON: If script is embedded-beats mode, delete the JSON and render again; still works.

---

## 17) Future Enhancements (not in scope)

- Choose between “embed beats” vs “load JSON” via UI toggle.
- Emit `.srt` subtitles from captions.
- Multi-scene templates and transitions.

---

## 18) After-Build Runbook (unchanged)

1. Create venv & install

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2. Export keys (Gemini required; ElevenLabs optional)

```
export GEMINI_API_KEY=sk-...
export ELEVENLABS_API_KEY=sk-...   # optional
export VOICE_ID=Rachel             # optional
```

3. Start server

```
uvicorn app:app --reload
```

4. Open UI

```
open http://127.0.0.1:8000
```

---

### Appendix A — Repro Script Requirements

- Single file defining `EconScene(Scene)`.
- Sets Manim config for 1080p30 (either via CLI or config in code comments).
- Reimplements tiny helpers:
  - axis creation (0..10, labels P/Q),
  - line constructors (D/S),
  - intersection calc + dashed helpers,
  - label placement with anti-overlap nudging,
  - beat player that parses the same DSL.
- Embeds beats inline (default) for portability; includes a commented option to load JSON if colocated.

