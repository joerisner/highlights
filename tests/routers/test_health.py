from fastapi.testclient import TestClient


def test_get_health(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200, response.text
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "UP"}
