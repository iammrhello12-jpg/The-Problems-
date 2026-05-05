import os
import sys
import pytest
from fastapi.testclient import TestClient

# Add src to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from agent.model import SimpleAgent
from agent.main import app

client = TestClient(app)

def test_model_prediction():
    agent = SimpleAgent()
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'intents.csv'))
    agent.train(data_path)

    result = agent.predict("hello")
    assert result["intent"] == "greeting"
    assert isinstance(result["response"], str)

    result = agent.predict("bye")
    assert result["intent"] == "goodbye"

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "AI Agent Assistant" in response.text

def test_api_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_api_chat():
    response = client.post("/chat", json={"text": "hi"})
    assert response.status_code == 200
    data = response.json()
    assert "intent" in data
    assert "response" in data
    assert data["intent"] == "greeting"
