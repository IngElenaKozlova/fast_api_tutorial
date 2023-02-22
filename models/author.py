from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float

from database import Base


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


class AuthorDB(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name_author = Column(String)
    surname_author = Column(String)
    age_author = Column(Integer)
    language_author = Column(String)
    rating = Column(Float, default=0.0)
