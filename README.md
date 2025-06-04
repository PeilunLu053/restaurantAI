
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
│   ├── main.py              # Entry point to start the FastAPI app
│   ├── routers/             # API route definitions (e.g., /copywriting, /editing)
│   │   ├── copywriting.py   # Generate restaurant/dish promotional content
│   │   ├── scripts.py       # Generate video shooting scripts
│   │   ├── editing.py       # Handle video editing operations
│   │   ├── publish.py       # Publish videos to platforms like TikTok, Xiaohongshu
│   │   └── feedback.py      # Video performance analytics and feedback
│   ├── services/            # Logic layer (LLM generation, video editing, API calls)
│   │   ├── llm_generator.py # Use Qwen2.5-7B Omni for script and copywriting
│   │   ├── ai_editor.py     # Automate editing using moviepy or ffmpeg
│   │   ├── platform_api.py  # Integrate with social media APIs
│   ├── utils/               # Utility functions (timing analysis, video tools)
│   │   ├── timing_analysis.py
│   │   └── video_tools.py
│   ├── schemas/             # Pydantic schemas for request/response validation
│   │   └── video_schema.py
│   └── config.py            # Environment and app configuration
│
├── frontend/                # ✅ Frontend UI (Flutter or Electron+Vue)
│   ├── flutter/             # Flutter project for mobile and web
│   │   ├── lib/
│   │   │   ├── main.dart
│   │   │   ├── routes/
│   │   │   ├── screens/
│   │   │   ├── widgets/
│   │   │   ├── services/
│   │   │   ├── models/
│   │   │   ├── constants/
│   │   │   └── utils/
│   │   ├── assets/
│   │   └── pubspec.yaml
│   └── electron-vue/        # Desktop app built with Electron + Vue
│       ├── src/
│       ├── public/
│       └── main.js
│
├── models/                  # ✅ AI model wrappers and configurations
│   ├── llm/                 # Language model (Qwen2.5-7B Omni)
│   │   └── qwen2.5-7b-omni/
│   ├── edit_model/          # Optional editing assistance models
│   │   └── auto_editor_model/
│   ├── qwen_wrapper.py      # Wrapper for Qwen2.5-7B Omni API
│   ├── cutgpt_wrapper.py    # Script generation wrapper (optional)
│   └── lora_config/         # LoRA config files (for model fine-tuning if needed)
│       └── config.json
│
├── data/                    # ✅ Uploaded media and intermediate files
│   ├── raw_videos/          # User-uploaded original video files
│   ├── images/              # Poster-style images or stills
│   ├── voices/              # Generated voice-over files (e.g., .mp3)
│   └── generated_scripts/   # AI-generated video scripts
│
├── output/                  # ✅ Final exported content and logs
│   ├── final_videos/        # Rendered videos (e.g., .mp4)
│   └── analytics/           # Video performance and backend logs
│
├── scripts/                 # ✅ Automation and testing scripts
│   ├── run_all.py           # One-click generation pipeline (script → edit → publish)
│   ├── launch_backend.sh    # Shell script to launch backend server
│   └── test_demo.ipynb      # Jupyter notebook for API demo/testing
│
├── .env.example             # Sample environment variable file
├── requirements.txt         # Python dependencies list
└── README.md                # Project documentation

```

---

## 🧪 Quickstart (Local Dev)

### 1. Clone the repository

```bash
git clone https://github.com/yourname/ai-restaurant-gen.git](https://github.com/PeilunLu053/restaurantAI.git
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

## 📦 Current Status

The repository contains an initial FastAPI backend and placeholder directories for frontend and models.

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

> Created with ❤️ by [PeilunLu](https://github.com/PeilunLu053)
