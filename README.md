# FastAPI Bot — Full Project

This is a more fully-featured FastAPI "bot" project ready to push to GitHub.

## Features
- JWT authentication (signup / login)
- User model (SQLModel + SQLite/Postgres compatible)
- `/bot` endpoint with simple bot logic and webhook-style handler
- Background tasks support
- Dockerfile + docker-compose (Postgres + Redis)
- Unit tests (pytest)
- GitHub Actions CI for tests
- Config via environment variables
- Logging and structured project layout

## Quickstart (dev)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

For production with Docker Compose:
```bash
docker compose up --build
```

## Files
See `app/` for the application code. Tests are in `tests/`.
