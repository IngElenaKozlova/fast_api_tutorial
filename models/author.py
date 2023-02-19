from pydantic import BaseModel


class Author(BaseModel):
    id: int
    name_author: str
    surname_author: str
    age_author: int
    language_author: str
    rating_author: float

    class Config:
        orm_mode = True


class PatchAuthor(BaseModel):
    name_author: str | None
    surname_author: str | None
    age_author: int | None
    language_author: str | None
    rating_author: float | None
