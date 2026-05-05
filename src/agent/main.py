from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from agent.model import SimpleAgent

app = FastAPI(title="AI Agent API", description="A simple AI Agent for intent classification and response generation.")

class Message(BaseModel):
    text: str

class Response(BaseModel):
    intent: str
    response: str

agent = SimpleAgent()

# Define paths relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# model.joblib is expected to be in the root directory relative to src/agent
ROOT_DIR = os.path.dirname(os.path.dirname(BASE_DIR))
model_path = os.path.join(ROOT_DIR, "model.joblib")
data_path = os.path.join(ROOT_DIR, "data", "intents.csv")
static_dir = os.path.join(BASE_DIR, "static")

if os.path.exists(model_path):
    agent.load(model_path)
else:
    # Fallback for development if model isn't trained yet
    if os.path.exists(data_path):
        agent.train(data_path)

@app.post("/chat", response_model=Response)
async def chat(message: Message):
    result = agent.predict(message.text)
    return result

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Serve static files
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_index():
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "AI Agent is online", "status": "ok"}
