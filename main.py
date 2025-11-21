from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.session import engine, init_db
from app.api.api_v1.api import api_router

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
def on_startup():
    # Create DB tables (SQLModel)
    init_db()

@app.get("/")
def root():
    return {"status": "ok", "app": settings.APP_NAME}
