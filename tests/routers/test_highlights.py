from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

mock_authors = [
    {"id": 1, "first_name": "John", "last_name": "Doe"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith"},
]


def test_get_highlights_with_no_params_raises_exception():
    response = client.get("/highlights")
    assert response.status_code == 400
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"detail": "Must request highlights by author, source, or tag!"}
