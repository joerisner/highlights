from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

mock_authors = [
    {"id": 1, "first_name": "John", "last_name": "Doe"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith"},
]


def test_get_all_authors_returns_list_of_authors():
    with patch("src.routers.authors.Author.find_all", return_value=mock_authors):
        response = client.get("/authors")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        assert response.json() == mock_authors


def test_get_author_by_id_found():
    with patch("src.routers.authors.Author.find", return_value=mock_authors[0]):
        response = client.get("/authors/1")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        assert response.json() == mock_authors[0]


def test_get_author_by_id_not_found():
    with patch("src.routers.authors.Author.find", return_value=None):
        response = client.get("/authors/999")
        assert response.status_code == 404
        assert response.json() == {"detail": "Author not found."}
