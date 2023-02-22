from sqlalchemy.orm import Session

import models
from models.book import Book, BookDB
from models.author import Author, AuthorDB


def get_book(db: Session, book_id: int):
    return db.query(BookDB).filter(BookDB.id == book_id).first()


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BookDB).offset(skip).limit(limit).all()


def create_book(db: Session, book: models.book.Book):
    db_book = BookDB(author_name=book.author_name, book_name=book.book_name,
                     rating=book.rating, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_author(db: Session, author_id: int):
    return db.query(AuthorDB).filter(AuthorDB.id == author_id).first()


def get_all_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AuthorDB).offset(skip).limit(limit).all()


def create_author(db: Session, author: models.author.Author):
    db_author = AuthorDB(name=author.name, surname=author.surname,
                         age=author.age, language=author.language,
                         rating=author.rating)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
