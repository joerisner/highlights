from fastapi import APIRouter, HTTPException

from ..models.author import Author, find_author, find_authors

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("")
def get_authors() -> list[Author]:
    """
    Show a list of all authors.
    """
    return find_authors()


@router.get("/{author_id}")
def get_author(author_id: int) -> Author:
    """
    Show a single author by id.
    """
    author = find_author(author_id)

    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")

    return author
