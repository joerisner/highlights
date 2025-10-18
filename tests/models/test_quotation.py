import pytest

from src.models.quotation import Quotation

pytestmark = pytest.mark.usefixtures("mock_find_all_quotations")


def test_find_all_quotations_from_data_file(mock_quotations):
    result = Quotation.find_all()
    assert result == mock_quotations


def test_find_quotation_by_id():
    result = Quotation.find(2)
    assert result == {
        "id": 2,
        "body": "I am faster than 80 percent of all snakes.",
        "metadata": "Chapter 2",
        "author_id": 2,
        "source_id": 2,
        "tag_ids": [1],
    }


def test_find_quotation_by_id_is_none_when_not_found():
    result = Quotation.find(9999)
    assert result is None


def test_find_by_params_with_no_attrs_returns_all_quotations(mock_quotations):
    result = Quotation.find_by_params()
    assert result == mock_quotations


def test_find_by_params_with_author_id_returns_quotations():
    result = Quotation.find_by_params(author_id=3)  # type: ignore
    assert result == [
        {
            "id": 3,
            "body": "I consider myself a good person...but I'm gonna try to make him cry.",
            "metadata": "Chapter 3",
            "author_id": 3,
            "source_id": 3,
            "tag_ids": [2],
        }
    ]


def test_find_by_params_with_source_id_returns_quotations():
    result = Quotation.find_by_params(source_id=2)  # type: ignore
    assert result == [
        {
            "id": 2,
            "body": "I am faster than 80 percent of all snakes.",
            "metadata": "Chapter 2",
            "author_id": 2,
            "source_id": 2,
            "tag_ids": [1],
        }
    ]


def test_find_by_params_with_tag_id_returns_quotations():
    result = Quotation.find_by_params(tag_id=2)  # type: ignore
    assert result == [
        {
            "id": 1,
            "body": "Dinkin' flicka.",
            "metadata": "Chapter 1",
            "author_id": 1,
            "source_id": 1,
            "tag_ids": [1, 2],
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
