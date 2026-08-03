import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.usefixtures("mock_find_all_authors")


def test_get_all_authors_returns_list_of_authors(client: TestClient, mock_authors):
    response = client.get("/authors")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == mock_authors


def test_get_author_by_id_found(client: TestClient):
    response = client.get("/authors/1")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"id": 1, "first_name": "Michael", "last_name": "Scott"}


def test_get_author_by_id_not_found(client: TestClient):
    response = client.get("/authors/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Author not found"}
