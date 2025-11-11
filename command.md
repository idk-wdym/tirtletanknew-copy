python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

manim --version
ffmpeg -version

export GEMINI_API_KEY="AIzaSyDka9Gzn8gN1ork5iPgrCHxtdtGoiKASfs"
export ELEVENLABS_API_KEY="sk_4cb4513b9a6c7366a95a31014287a896d55f2055e0f7e7a4"
export VOICE_ID="Rachel"

uvicorn app:app --reload
