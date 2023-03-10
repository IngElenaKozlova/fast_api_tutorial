from pydantic import BaseModel


class Book(BaseModel):
    id: int
    author_name: str
    book_name: str
    rating: float
    description: str


class PatchBook(BaseModel):
    author_name: str | None
    book_name: str | None
    rating: float | None
    description: str | None