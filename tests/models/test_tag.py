import pytest

from src.models.tag import Tag

pytestmark = pytest.mark.usefixtures("mock_find_all_tags")


def test_find_all_tags_from_data_file(mock_tags):
    result = Tag.find_all()
    assert result == mock_tags


def test_find_tag_by_id():
    result = Tag.find(2)
    assert result == {"id": 2, "name": "inappropriate"}


def test_find_tag_by_id_is_none_when_not_found():
    result = Tag.find(999)
    assert result is None
