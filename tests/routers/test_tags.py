import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)
pytestmark = pytest.mark.usefixtures("mock_find_all_tags")


def test_get_all_tags_returns_list_of_tags(mock_tags):
    response = client.get("/tags")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == mock_tags


def test_get_tag_by_id_found():
    response = client.get("/tags/1")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"id": 1, "name": "comedically-humorous"}


def test_get_tag_by_id_not_found():
    response = client.get("/tags/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Tag not found."}
