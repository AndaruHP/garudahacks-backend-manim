import os
import shutil
import uuid as uuidlib
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import httpx
import subprocess
import json
import re
import codecs
import datetime
from fastapi.middleware.cors import CORSMiddleware
import logging
import openai

# Ambil allowed origins dari environment variable
allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
allowed_origins = [origin.strip() for origin in allowed_origins]

app = FastAPI()

# Tambahkan CORS agar API bisa diakses dari frontend/domain yang diizinkan
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/output", StaticFiles(directory="output"), name="output")
load_dotenv()

# Simulasi database sederhana (pakai dict, ganti dengan DB asli jika perlu)
user_request_count = {}

# Helper: hitung request ke berapa untuk user
def get_user_request_count(user_id):
    count = user_request_count.get(user_id, 0) + 1
    user_request_count[user_id] = count
    return count

# openai
async def call_gpt_api(prompt, context):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2048,
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error saat call GPT: {e}")
        raise

# Helper: kirim prompt ke Gemini
async def call_gemini_api(prompt, context):
    api_key = os.getenv("GEMINI_API_KEY")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": context + "\n" + prompt}]}
        ]
    }
    params = {"key": api_key}
    try:
        async with httpx.AsyncClient(timeout=600.0) as client:
            resp = await client.post(url, headers=headers, params=params, json=payload)
            resp.raise_for_status()
            return resp.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("Error saat call Gemini:", e)
        raise

def clean_markdown_block(text):
    # Hilangkan blok markdown ```json ... ``` di awal dan akhir
    return re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.IGNORECASE | re.MULTILINE)

def fix_invalid_json(text):
    # Ganti newline mentah dengan \\n agar valid untuk json.loads
    return text.replace('\r\n', '\\n').replace('\n', '\\n')


def extract_json_code(response_text):
    """
    Ekstrak JSON yang mengandung key 'code' dari response LLM.
    Return kode python dari field 'code', atau None jika tidak ditemukan.
    """
    # Bersihkan blok markdown jika ada
    cleaned = clean_markdown_block(response_text)
    # Coba parse langsung
    try:
        obj = json.loads(cleaned)
        if "code" in obj:
            return obj["code"]
    except Exception:
        pass
    # Jika gagal, cari substring mirip JSON
    matches = re.findall(r'\{.*?"code"\s*:\s*".*?"\s*\}', cleaned, re.DOTALL)
    for match in matches:
        try:
            obj = json.loads(match)
            if "code" in obj:
                return obj["code"]
        except Exception:
            continue
    return None

def ensure_json_starts_with_brace(text):
    idx = text.find('{')
    if idx != -1:
        return text[idx:]
    return text

def fix_newline_in_code_value(json_str):
    # Ganti newline mentah di dalam value "code" menjadi \\n
    # Hanya berlaku untuk value "code"
    return re.sub(
        r'("code"\s*:\s*")((?:[^"\\]|\\.)*)"',
        lambda m: m.group(1) + m.group(2).replace('\n', '\\n') + '"',
        json_str,
        flags=re.DOTALL
    )

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    user_id = data["user_id"]
    prompt = data["prompt"]
    bahasa = data["bahasa"]

    if not user_id or not prompt:
        logging.error(f"Request missing user_id or prompt: {data}")
        return JSONResponse({"error": "user_id dan prompt wajib ada"}, status_code=400)

    logging.info(f"Received generate request: user_id={user_id}, prompt={prompt}, bahasa={bahasa}")

    # 1. Hitung request ke berapa
    req_count = get_user_request_count(user_id)
    # 1. Hitung folder_name dengan uuid dan timestamp
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    folder_name = f"{user_id}_{now}"
    output_folder_path = os.path.join("output", folder_name)
    # media_folder_path = os.path.join("media", folder_name)
    os.makedirs(output_folder_path, exist_ok=True)
    # os.makedirs(media_folder_path, exist_ok=True)

    # 2. Siapkan konteks untuk Gemini
    context = (
        "Berikan hanya response JSON tanpa pembuka apapun.\n"
        "Format: {\"code\": \"<kode python manim lengkap dari import sampai akhir>\"}\n"
        "Target pembelajar adalah anak SD, gunakan konsep yang sangat dasar.\n"
        "Pertanyaan dijawab dari dasar sehingga yang belum mengerti matematika dasar bisa mengerti ataupun bisa diberikan cara berpikir.\n"
        "Kode Python harus menggunakan library manim dan wajib menggunakan manim_voiceover.\n"
        "Gunakan class utama yang mewarisi dari VoiceoverScene, bukan Scene.\n"
        "Kode wajib menggunakan AzureService dari manim_voiceover.\n"
        "Import yang wajib digunakan di awal:\n"
        "from manim import *\n"
        "from manim_voiceover import VoiceoverScene\n"
        "from manim_voiceover.services.azure import AzureService\n"
        "Gunakan konfigurasi AzureService sebagai berikut:\n"
        "self.set_speech_service(\n"
        "    AzureService(\n"
        "        voice=\"id-ID-GadisNeural\", \n"
        "        style=\"general\", \n"
        "        azure_key=os.getenv(\"AZURE_SUBSCRIPTION_KEY\"), \n"
        "        region=os.getenv(\"AZURE_SERVICE_REGION\")\n"
        "    )\n"
        ")\n"
        "Setiap scene harus memiliki penjelasan audio dengan with self.voiceover(...):\n"
        "Contoh penggunaan AzureService dan audio:\n"
        "self.set_speech_service(\n"
        "    AzureService(\n"
        "        voice=\"id-ID-GadisNeural\",\n"
        "        style=\"general\",\n"
        "        azure_key=os.getenv(\"AZURE_SUBSCRIPTION_KEY\"),\n"
        "        region=os.getenv(\"AZURE_SERVICE_REGION\")\n"
        "    )\n"
        ")\n"
        "with self.voiceover(\"Ini adalah lingkaran merah.\"):\n"
        "    self.play(Create(Circle(color=RED)))\n"
        "Hanya gunakan mobject dasar seperti Circle, Square, Rectangle, Line, Dot, Text, MathTex.\n"
        "Gunakan animasi dasar: Create, Write, FadeIn, FadeOut, Transform, Wait.\n"
        "Gunakan warna dasar seperti RED, BLUE, GREEN, YELLOW.\n"
        "Gunakan posisi sederhana seperti UP, DOWN, LEFT, RIGHT atau koordinat seperti (2, 0, 0).\n"
        "Hindari method yang kompleks seperti get_grid, gunakan VGroup dan arrange_in_grid jika perlu.\n"
        "Jangan gunakan Tex, hanya MathTex untuk rumus.\n"
        "Pastikan semua kode memiliki indentasi 4 spasi, tidak menggunakan tab.\n"
        "Hapus objek dari layar setelah tidak dipakai.\n"
    )
    if bahasa:
        context += f"Gunakan bahasa: {bahasa}.\n"
    context += (
        "Jika bahasa adalah indonesia, maka gunakan voice id-ID-GadisNeural.\n"
        "Jika bahasa adalah inggris, maka gunakan voice en-US-AvaMultilingualNeural.\n"
        "Style audio adalah general.\n"
        "Permintaan user: "
    )


    # 3. Panggil Gemini API
    full_prompt = context + prompt
    try:
        # Setelah dapat response dari Gemini
        # code_json = await call_gemini_api(full_prompt, "")
        code_json = await call_gpt_api(prompt, context)
        logging.info(f"Gemini raw response: {repr(code_json)}")

        # 1. Bersihkan blok markdown
        cleaned = clean_markdown_block(code_json)
        # 2. Pastikan mulai dari '{'
        json_ready = ensure_json_starts_with_brace(cleaned)
        # 3. Perbaiki newline mentah di value 'code'
        json_fixed = fix_newline_in_code_value(json_ready)
        # 4. Parse JSON
        obj = json.loads(json_fixed)
        code = obj["code"]
    except Exception as e:
        logging.error(f"Error parsing Gemini response: {e}")
        return JSONResponse({"error": "Gagal memproses kode dari Gemini"}, status_code=500)

    # 4. Simpan kode ke file di output/{folder_name}
    py_filename_full = os.path.join(output_folder_path, "generated.py")
    with open(py_filename_full, "w") as f:
        f.write(code)
    logging.info(f"Saved generated.py to {py_filename_full}")

    # 5. Cari nama class utama (misal: class NamaScene(VoiceoverScene):)
    match = re.search(r"class\s+(\w+)\s*\(", code)
    if not match:
        logging.error("Tidak ditemukan class utama di kode Gemini")
        return JSONResponse({"error": "Tidak ditemukan class utama di kode Gemini"}, status_code=400)
    class_name = match.group(1)

    # 6. Jalankan manim dari output/{folder_name}, hasilkan video ke media/{folder_name}
    try:
        subprocess.run(
            [
                "/root/manimations/.venv/bin/manim", "-pqh", "generated.py", class_name,
                "--output_file", "result.mp4"
            ],
            check=True,
            cwd=output_folder_path
        )
        logging.info(f"Manim render success for {py_filename_full}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Gagal menjalankan manim: {e}")
        return JSONResponse({"error": f"Gagal menjalankan manim: {e}"}, status_code=500)

    # 7. Ambil path video hasil manim
    video_path = os.path.join(
        output_folder_path, "media", "videos", "generated", "1080p60", "result.mp4"
    )
    if not os.path.exists(video_path):
        logging.error(f"Video tidak ditemukan: {video_path}")
        return JSONResponse({"error": "Video tidak ditemukan, proses render gagal."}, status_code=500)

    video_url = f"/output/{folder_name}/media/videos/generated/1080p60/result.mp4"
    video_html = f'<video controls width="640" src="{video_url}"></video>'

    logging.info(f"Video generated: {video_url}")

    try:
        compile(code, py_filename_full, 'exec')
    except IndentationError as e:
        logging.error(f"Indentation error in generated code: {e}")
        return JSONResponse({"error": f"Indentation error in generated code: {e}"}, status_code=500)
    except SyntaxError as e:
        logging.error(f"Syntax error in generated code: {e}")
        return JSONResponse({"error": f"Syntax error in generated code: {e}"}, status_code=500)

    return {
        "message": "Video berhasil dibuat!",
        "video_url": video_url,
        "video_html": video_html,
        "prompt": prompt,
        "folder_name": folder_name
    }