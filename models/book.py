from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class BaseAuthor(BaseModel):
    id: int
    age: int
    name: str
    surname: str
    language: str
    rating: float

    class Config:
        orm_mode = True


class BaseBook(BaseModel):
    book_name: str
    rating: float
    description: str
    class Config:
        schema_extra = {
            "example": {
                "book_name": "Harry Potter and the Philosopher's Stone",
                "rating": 10.0,
                "description": "The best book ever"
            }
        }

class PostBook(BaseBook):
    author_id: int


class PostBookResponse(BaseBook):
    id: int
    author: BaseAuthor

    class Config:
        orm_mode = True


class PutBook(PostBook):
    id: int


class PatchBook(BaseModel):
    id: int
    author_id: str | None
    book_name: str | None
    rating: float | None
    description: str | None


class BookDB(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    book_name = Column(String)
    rating = Column(Float, default=0.0)
    description = Column(String)

    author = relationship("AuthorDB", back_populates="books")
