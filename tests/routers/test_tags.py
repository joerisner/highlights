from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

mock_tags = [
    {"id": 1, "name": "grace"},
    {"id": 2, "name": "inspiration"},
]


def test_get_all_tags_returns_list_of_tags():
    with patch("src.routers.tags.Tag.find_all", return_value=mock_tags):
        response = client.get("/tags")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        assert response.json() == mock_tags


def test_get_tag_by_id_found():
    with patch("src.routers.tags.Tag.find", return_value=mock_tags[0]):
        response = client.get("/tags/1")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        assert response.json() == mock_tags[0]


def test_get_tag_by_id_not_found():
    with patch("src.routers.tags.Tag.find", return_value=None):
        response = client.get("/tags/999")
        assert response.status_code == 404
        assert response.json() == {"detail": "Tag not found."}
