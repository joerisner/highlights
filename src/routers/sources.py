from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models.source import Source


class SourceRecord(BaseModel):
    id: int
    completed: bool
    title: str
    type: str


router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("")
def get_sources() -> list[SourceRecord]:
    """
    Show a list of all sources.
    """
    return Source.find_all()


@router.get("/{source_id}")
def get_source(source_id: int) -> SourceRecord:
    """
    Show a single source by id.
    """
    source = Source.find(source_id)

    if not source:
        raise HTTPException(status_code=404, detail="Source not found.")

    return source
