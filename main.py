from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI Bot")

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "Bot is running!"}

@app.post("/bot")
def bot_endpoint(msg: Message):
    reply = f"You said: {msg.text}"
    return {"reply": reply}
