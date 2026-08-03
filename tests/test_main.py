from fastapi.testclient import TestClient


def test_get_root(client: TestClient):
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "Application is running."}


def test_openapi_docs_hidden_when_not_configured(client: TestClient):
    docs_response = client.get("/docs")
    redoc_response = client.get("/redoc")
    open_api_response = client.get("/openapi.json")

    assert docs_response.status_code == 404
    assert docs_response.json() == {"detail": "Not Found"}
    assert redoc_response.status_code == 404
    assert redoc_response.json() == {"detail": "Not Found"}
    assert open_api_response.status_code == 404
    assert open_api_response.json() == {"detail": "Not Found"}
