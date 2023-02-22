from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float

from database import Base


class Book(BaseModel):
    author_name: str
    book_name: str
    rating: float
    description: str

    class Config:
        orm_mode = True


class PatchBook(BaseModel):
    author_name: str | None
    book_name: str | None
    rating: float | None
    description: str | None


class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    author_name = Column(String, unique=True)
    book_name = Column(String)
    rating = Column(Float, default=0.0)
    description = Column(String)
