from unittest.mock import patch

import pytest


@pytest.fixture
def mock_authors():
    return [
        {"id": 1, "first_name": "Michael", "last_name": "Scott"},
        {"id": 2, "first_name": "Dwight", "last_name": "Schrute"},
        {"id": 3, "first_name": "Oscar", "last_name": "Martinez"},
    ]


@pytest.fixture
def mock_sources():
    return [
        {"id": 1, "completed": False, "title": "Season 1", "type": "SERIES"},
        {"id": 2, "completed": True, "title": "Season 2", "type": "TELEVISION"},
        {"id": 3, "completed": True, "title": "Season 3", "type": "TELEVISION"},
    ]


@pytest.fixture
def mock_tags():
    return [
        {"id": 1, "name": "comedically-humorous"},
        {"id": 2, "name": "inappropriate"},
        {"id": 3, "name": "sarcastic"},
    ]


@pytest.fixture
def mock_quotations():
    return [
        {
            "id": 1,
            "body": "Dinkin' flicka.",
            "metadata": "Chapter 1",
            "author_id": 1,
            "source_id": 1,
            "tag_ids": [1, 2],
        },
        {
            "id": 2,
            "body": "I am faster than 80 percent of all snakes.",
            "metadata": "Chapter 2",
            "author_id": 2,
            "source_id": 2,
            "tag_ids": [1],
        },
        {
            "id": 3,
            "body": "I consider myself a good person...but I'm gonna try to make him cry.",
            "metadata": "Chapter 3",
            "author_id": 3,
            "source_id": 3,
            "tag_ids": [2],
        },
    ]


@pytest.fixture
def mock_find_all_authors(mock_authors):
    with patch("src.models.author.Author.find_all", return_value=mock_authors) as authors:
        yield authors


@pytest.fixture
def mock_find_all_sources(mock_sources):
    with patch("src.models.source.Source.find_all", return_value=mock_sources) as sources:
        yield sources


@pytest.fixture
def mock_find_all_tags(mock_tags):
    with patch("src.models.tag.Tag.find_all", return_value=mock_tags) as tags:
        yield tags


@pytest.fixture
def mock_find_all_quotations(mock_quotations):
    with patch("src.models.quotation.Quotation.find_all", return_value=mock_quotations) as quotations:
        yield quotations
