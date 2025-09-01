from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "Application is running."}
