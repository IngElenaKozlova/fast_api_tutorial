from sqlalchemy import Column, Integer, String, Float

from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    author_name = Column(String, unique=True)
    book_name = Column(String)
    rating = Column(Float, default=0.0)
    description = Column(String)
