import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predictions_endpoint():
    response = client.get("/api/v1/predictions")
    assert response.status_code == 200
    assert "predictions" in response.json()
