from src.models.author import Author


def test_find_all_authors_from_data_file():
    authors = Author.find_all()
    assert isinstance(authors, list)
    assert len(authors) > 1


def test_find_author_by_id():
    author = Author.find(1)
    assert isinstance(author, dict)
    assert list(author.keys()) == ["id", "first_name", "last_name"]


def test_find_author_by_id_is_none_when_not_found():
    author = Author.find(999)
    assert author is None
