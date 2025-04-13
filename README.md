
# 🍱 AI-Powered Restaurant Content Generator (Project R-AIGEN)

## 🚀 Overview

**R-AIGEN** is a full-stack AI platform designed to help small and medium-sized restaurant owners automatically generate digital promotional materials. From keyword input to export-ready videos, the system automates:

- Promotional copywriting
- Short video scripting
- Voiceover narration
- Smart video editing

This project empowers restaurant teams without editing experience to launch social-ready content with just a few clicks.

---

## 🧠 Core MVP Features

- ✅ AI-generated promotional copy in various tones
- ✅ Short video scripts with visual storyboard suggestions
- ✅ Edge-TTS voiceover generation (local/offline supported)
- ✅ Automatic video editing with user-uploaded footage
- ✅ Export final videos (MP4), ready for TikTok, WeChat, etc.

---

## 🧱 Tech Stack

| Layer       | Technology |
|-------------|------------|
| Frontend    | Flutter (Cross-platform) or Electron + Vue |
| Backend     | FastAPI (Python 3.10+) |
| AI Models   | Qwen2.5-Omni (multi-modal LLM), Edge-TTS, MoviePy, FFmpeg |
| Data Layer  | JSON + SQLite |
| Deployment  | Local (Windows/macOS), Docker support planned |

---

## 📁 Project Structure

```
ai-restaurant-gen/
├── backend/                 # ✅ Backend service (FastAPI APIs and business logic)
│   ├── main.py              # Project entry point – starts FastAPI app
│   ├── routes/              # API route definitions (e.g., /generate, /tts, /cut)
│   │   └── video.py
│   ├── services/            # Logic layer: model inference, editing, TTS, etc.
│   │   ├── generator.py     # Calls Qwen2.5 for copy/script generation
│   │   ├── tts.py           # Handles Edge-TTS voice synthesis
│   │   └── editor.py        # Automates video editing with moviepy/ffmpeg
│   └── schemas/             # Pydantic data models for request/response validation
│       └── video_schema.py
│
├── frontend/                # ✅ Frontend UI (Flutter or Electron + Vue)
│   ├── flutter/             # Flutter project for mobile & web support
│   └── electron-vue/        # Electron desktop app (recommended for MVP)
│       ├── src/
│       ├── public/
│       └── main.js
│
├── models/                  # ✅ Model wrappers and configurations
│   ├── qwen_wrapper.py      # Qwen2.5 or DeepSeek model API wrapper
│   ├── cutgpt_wrapper.py    # Wrapper for LLM-based cut/script generation
│   └── lora_config/         # LoRA training configurations (if needed)
│       └── config.json
│
├── data/                    # ✅ Uploaded media and input/output files
│   ├── uploads/             # User-uploaded raw video footage
│   ├── images/              # Uploaded image materials / poster shots
│   └── voices/              # Generated voice files (.mp3)
│
├── output/                  # ✅ Final exported content and logs
│   ├── videos/              # Output videos (.mp4)
│   └── logs/                # Backend logs and error reports
│
├── scripts/                 # ✅ Automation tools and batch scripts
│   ├── run_all.py           # One-click pipeline: from generation to editing
│   ├── launch_backend.sh    # Script to launch backend server
│   └── test_demo.ipynb      # Jupyter notebook for API testing/demo
│
├── .env.example             # Environment variable sample
├── requirements.txt         # Python dependencies
└── README.md                # This document
```

---

## 🧪 Quickstart (Local Dev)

### 1. Clone the repository

```bash
git clone https://github.com/yourname/ai-restaurant-gen.git
cd ai-restaurant-gen
```

### 2. Create a Python environment

```bash
conda create -n r-aigen python=3.10
conda activate r-aigen
pip install -r requirements.txt
```

### 3. Start backend server

```bash
cd backend
uvicorn main:app --reload
```

---

## 🔮 Roadmap

- [ ] End-to-end MVP: from keyword input to video export
- [ ] UI: build desktop (Electron) or cross-platform (Flutter) frontend
- [ ] Support multiple voice styles and languages
- [ ] Subtitle and visual transition templates
- [ ] SaaS deployment support for multi-user access

---

## 📄 License

This project is licensed under the **Apache License 2.0**.  
It includes open-source tools such as:

- Qwen2.5-Omni (by Alibaba)
- Edge-TTS (Microsoft)
- MoviePy & FFmpeg (MIT/BSD)

You are free to use, modify, and redistribute this project under the terms of the Apache 2.0 license.

---

> Created with ❤️ by [PeilunLu](https://github.com/yourname)
