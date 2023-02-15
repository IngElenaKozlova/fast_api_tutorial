from sqlalchemy.orm import Session

import models
from sql_book import Book


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: models.book.Book):
    db_book = Book(author_name=book.author_name, book_name=book.book_name,
                   rating=book.rating, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
