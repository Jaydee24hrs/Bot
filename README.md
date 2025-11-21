# FastAPI Bot

A simple FastAPI bot you can deploy anywhere or upload directly to GitHub.

## 🚀 Features
- `/` health check
- `/bot` POST endpoint to reply to messages

## 📦 Install
```bash
pip install -r requirements.txt
```

## ▶️ Run
```bash
uvicorn main:app --reload
```

## 🐳 Docker
```bash
docker build -t fastapi-bot .
docker run -p 8000:8000 fastapi-bot
```
