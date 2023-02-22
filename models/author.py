from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float

from database import Base


class Author(BaseModel):
    name: str
    surname: str
    age: int
    language: str
    rating: float

    class Config:
        orm_mode = True


class PatchAuthor(BaseModel):
    name: str | None
    surname: str | None
    age: int | None
    language: str | None
    rating: float | None


class AuthorDB(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    language = Column(String)
    rating = Column(Float, default=0.0)
