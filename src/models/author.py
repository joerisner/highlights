from pydantic import BaseModel

from .base import Base


class AuthorRecord(BaseModel):
    id: int
    first_name: str
    last_name: str


class Author(Base):
    DATA_FILE = "authors.json"
