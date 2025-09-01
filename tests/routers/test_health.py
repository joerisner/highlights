from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "UP"}
