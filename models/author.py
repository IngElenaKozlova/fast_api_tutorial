from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class BookWithoutID(BaseModel):
    book_name: str
    rating: float
    description: str

    class Config:
        orm_mode = True


class BaseAuthor(BaseModel):
    age: int
    name: str
    surname: str
    language: str
    rating: float
    class Config:
        schema_extra = {
            "example": {
                "age": 24,
                "name": "Nikolas",
                "surname": "Flamel",
                "language": "Eng",
                "rating": 9.8
            }
        }


class AuthorGetResponse(BaseAuthor):
    id: int
    books: list[BookWithoutID] = []

    class Config:
        orm_mode = True


class PutAuthor(BaseAuthor):
    id: int


class PatchAuthor(BaseModel):
    id: int
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

    books = relationship("BookDB", back_populates="author")

    def __repr__(self):
        return f"{self.id}, {self.books}"
