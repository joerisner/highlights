import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)
pytestmark = pytest.mark.usefixtures("mock_find_all_sources")


def test_get_all_sources_returns_list_of_sources(mock_sources):
    response = client.get("/sources")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == mock_sources


def test_get_source_by_id_found():
    response = client.get("/sources/1")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"id": 1, "completed": False, "title": "Season 1", "type": "SERIES"}


def test_get_source_by_id_not_found():
    response = client.get("/sources/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Source not found."}
