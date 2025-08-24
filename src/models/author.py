import json
from pathlib import Path

from pydantic import BaseModel


class Author(BaseModel):
    id: int
    first_name: str
    last_name: str


def _load_authors_data() -> list[dict]:
    """
    Load authors data from the authors.json file.
    """
    authors_file = Path(__file__).parent.parent / "data" / "authors.json"
    with open(authors_file) as file:
        return json.load(file)["authors"]


def find_authors() -> list[Author]:
    """
    Return a list of all authors.
    """
    authors_data = _load_authors_data()

    return [
        Author(id=author["id"], first_name=author["firstName"], last_name=author["lastName"]) for author in authors_data
    ]


def find_author(id: int) -> Author:
    """
    Find and return a single author by id.
    """
    authors_data = _load_authors_data()
    author_data = next((author for author in authors_data if author["id"] == id), None)

    if author_data:
        return Author(id=author_data["id"], first_name=author_data["firstName"], last_name=author_data["lastName"])

    return None
