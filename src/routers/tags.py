from fastapi import APIRouter, HTTPException, status
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
    tags = Tag.find_all()
    return [TagRecord(id=tag["id"], name=tag["name"]) for tag in tags]


@router.get("/{tag_id}")
def get_tag(tag_id: int) -> TagRecord:
    """
    Show a single tag by id.
    """
    tag = Tag.find(tag_id)

    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")

    return TagRecord(id=tag["id"], name=tag["name"])
