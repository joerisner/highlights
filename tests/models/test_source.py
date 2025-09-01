from src.models.source import Source


def test_find_all_sources_from_data_file():
    sources = Source.find_all()
    assert isinstance(sources, list)
    assert len(sources) > 1


def test_find_source_by_id():
    source = Source.find(1)
    assert isinstance(source, dict)
    assert list(source.keys()) == ["id", "completed", "title", "type"]


def test_find_source_by_id_is_none_when_not_found():
    source = Source.find(999)
    assert source is None
