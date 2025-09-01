from unittest.mock import patch

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

mock_sources = [
    {"id": 1, "completed": False, "title": "No Easy Day", "type": "BOOK"},
    {"id": 2, "completed": True, "title": "Providence", "type": "BOOK"},
]


def test_get_all_sources_returns_list_of_sources():
    with patch("src.routers.sources.Source.find_all", return_value=mock_sources):
        response = client.get("/sources")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        assert response.json() == mock_sources


def test_get_source_by_id_found():
    with patch("src.routers.sources.Source.find", return_value=mock_sources[0]):
        response = client.get("/sources/1")
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"
        assert response.json() == mock_sources[0]


def test_get_source_by_id_not_found():
    with patch("src.routers.sources.Source.find", return_value=None):
        response = client.get("/sources/999")
        assert response.status_code == 404
        assert response.json() == {"detail": "Source not found."}
