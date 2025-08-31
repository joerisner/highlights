from fastapi import APIRouter, HTTPException

from ..models.author import Author, AuthorRecord

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("")
def get_authors() -> list[AuthorRecord]:
    """
    Show a list of all authors.
    """
    return Author.find_all()


@router.get("/{author_id}")
def get_author(author_id: int) -> AuthorRecord:
    """
    Show a single author by id.
    """
    author = Author.find(author_id)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")

    return author
