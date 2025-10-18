from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..models.author import Author


class AuthorRecord(BaseModel):
    id: int
    first_name: str
    last_name: str


router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("")
def get_authors() -> list[AuthorRecord]:
    """
    Show a list of all authors.
    """
    authors = Author.find_all()
    return [
        AuthorRecord(id=author["id"], first_name=author["first_name"], last_name=author["last_name"])
        for author in authors
    ]


@router.get("/{author_id}")
def get_author(author_id: int) -> AuthorRecord:
    """
    Show a single author by id.
    """
    author = Author.find(author_id)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")

    return AuthorRecord(id=author["id"], first_name=author["first_name"], last_name=author["last_name"])
