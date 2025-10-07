import pytest

from src.models.author import Author

pytestmark = pytest.mark.usefixtures("mock_find_all_authors")


def test_find_all_authors_from_data_file(mock_authors):
    result = Author.find_all()
    assert result == mock_authors


def test_find_author_by_id():
    result = Author.find(3)
    assert result == {"id": 3, "first_name": "Oscar", "last_name": "Martinez"}


def test_find_author_by_id_is_none_when_not_found():
    result = Author.find(999)
    assert result is None
