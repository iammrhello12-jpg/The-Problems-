from fastapi import FastAPI
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
model_path = "model.joblib"

if os.path.exists(model_path):
    agent.load(model_path)
else:
    # Fallback for development if model isn't trained yet
    data_path = "data/intents.csv"
    if os.path.exists(data_path):
        agent.train(data_path)

@app.get("/")
async def root():
    return {"message": "AI Agent is online", "status": "ok"}

@app.post("/chat", response_model=Response)
async def chat(message: Message):
    result = agent.predict(message.text)
    return result

@app.get("/health")
async def health():
    return {"status": "healthy"}
