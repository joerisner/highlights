from src.models.tag import Tag


def test_find_all_tags_from_data_file():
    tags = Tag.find_all()
    assert isinstance(tags, list)
    assert len(tags) > 1


def test_find_tag_by_id():
    tag = Tag.find(1)
    assert isinstance(tag, dict)
    assert list(tag.keys()) == ["id", "name"]


def test_find_tag_by_id_is_none_when_not_found():
    tag = Tag.find(999)
    assert tag is None
