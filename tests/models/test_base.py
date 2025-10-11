from src.models.author import Author
from src.models.quotation import Quotation
from src.models.source import Source
from src.models.tag import Tag


def test_authors_have_unique_ids():
    results = Author.find_all()
    all_ids = [author["id"] for author in results]
    unique_ids = set(all_ids)
    assert len(all_ids) == len(unique_ids)


def test_quotations_have_unique_ids():
    results = Quotation.find_all()
    all_ids = [quotation["id"] for quotation in results]
    unique_ids = set(all_ids)
    assert len(all_ids) == len(unique_ids)


def test_sources_have_unique_ids():
    results = Source.find_all()
    all_ids = [source["id"] for source in results]
    unique_ids = set(all_ids)
    assert len(all_ids) == len(unique_ids)


def test_tags_have_unique_ids():
    results = Tag.find_all()
    all_ids = [tag["id"] for tag in results]
    unique_ids = set(all_ids)
    assert len(all_ids) == len(unique_ids)
