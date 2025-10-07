import pytest

from src.models.source import Source

pytestmark = pytest.mark.usefixtures("mock_find_all_sources")


def test_find_all_sources_from_data_file(mock_sources):
    result = Source.find_all()
    assert result == mock_sources


def test_find_source_by_id():
    result = Source.find(1)
    assert result == {"id": 1, "completed": False, "title": "Season 1", "type": "SERIES"}


def test_find_source_by_id_is_none_when_not_found():
    result = Source.find(999)
    assert result is None
