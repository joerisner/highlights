from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models.tag import Tag


class TagRecord(BaseModel):
    id: int
    name: str


router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("")
def get_tags() -> list[TagRecord]:
    """
    Show a list of all tags.
    """
    return Tag.find_all()


@router.get("/{tag_id}")
def get_tag(tag_id: int) -> TagRecord:
    """
    Show a single tag by id.
    """
    tag = Tag.find(tag_id)

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found.")

    return tag
