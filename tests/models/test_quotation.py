from src.models.quotation import Quotation


def test_find_all_quotations_from_data_file():
    quotations = Quotation.find_all()
    assert isinstance(quotations, list)
    assert len(quotations) > 1


def test_find_quotation_by_id():
    quotation = Quotation.find(1)
    assert isinstance(quotation, dict)
    assert list(quotation.keys()) == ["id", "body", "metadata", "author_id", "source_id", "tag_ids"]


def test_find_quotation_by_id_is_none_when_not_found():
    quotation = Quotation.find(9999)
    assert quotation is None
