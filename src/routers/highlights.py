import random

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models.author import Author
from ..models.quotation import Quotation
from ..models.source import Source
from ..models.tag import Tag

router = APIRouter(prefix="/highlights", tags=["highlights"])


class Highlight(BaseModel):
    author: str
    body: str
    source: str
    metadata: str
    tags: list[str]


def _generate_highlight(quotation: Quotation) -> Highlight:
    """
    Generate a highlight from a quotation record.
    """
    author = Author.find(quotation["author_id"])
    source = Source.find(quotation["source_id"])
    tags = [Tag.find(id).get("name", "") for id in quotation["tag_ids"]]

    return Highlight(
        author=f"{author['first_name']} {author['last_name']}",
        body=quotation["body"],
        source=source["title"],
        metadata=quotation["metadata"],
        tags=tags,
    )


@router.get("/")
def get_highlights(author: int | None = None, source: int | None = None, tag: int | None = None) -> list[Highlight]:
    """
    Show all highlights filtered by author, source, or tag.
    """
    if not author and not source and not tag:
        raise HTTPException(
            status_code=400,
            detail="Must request highlights by author, source, or tag!",
        )

    query_filter = {}
    if author:
        query_filter["author_id"] = int(author)
    if source:
        query_filter["source_id"] = int(source)
    if tag:
        query_filter["tag_id"] = int(tag)

    quotations = Quotation.find_by_params(**query_filter)

    if not quotations:
        raise HTTPException(status_code=404, detail="No quotations found")

    highlights = map(_generate_highlight, quotations)
    return list(highlights)


@router.get("/random")
def get_random_highlight() -> Highlight:
    """
    Get a random highlight.
    """
    quotations = Quotation.find_all()
    random_id = random.choice(quotations).get("id")
    quotation = Quotation.find(random_id)

    return _generate_highlight(quotation)
