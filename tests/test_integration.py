import pytest
from fastapi.testclient import TestClient
from api.main import app

def test_health_check_endpoint():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["status"] == "ok"
        assert json_data["model_loaded"] is True
