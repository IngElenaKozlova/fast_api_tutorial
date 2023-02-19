from sqlalchemy.orm import Session

import models
from sql_models.sql_book import Book
from sql_models.sql_author import Author


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


def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def get_all_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: models.author.Author):
    db_author = Author(name_author=author.name_author, surname_author=author.surname_author,
                       age_author=author.age_author, language_author=author.language_author,
                       rating_author=author.rating_author)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
