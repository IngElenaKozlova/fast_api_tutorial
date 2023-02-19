from sqlalchemy import Column, Integer, String, Float

from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name_author = Column(String)
    surname_author = Column(String)
    age_author = Column(Integer)
    language_author = Column(String)
    rating = Column(Float, default=0.0)
