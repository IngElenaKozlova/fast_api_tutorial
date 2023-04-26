from sqlalchemy.orm import Session

import models
from models.book import BookDB
from models.author import AuthorGetResponse, AuthorDB


def get_book(db: Session, book_id: int) -> BookDB:
    return db.query(BookDB).filter(BookDB.id == book_id).first()


def get_all_books(db: Session, skip: int = 0, limit: int = 100):
    r = db.query(BookDB).offset(skip).limit(limit).all()
    return r


def create_book(db: Session, book: models.book.PostBook):
    db_book = BookDB(author_id=book.author_id, book_name=book.book_name,
                     rating=book.rating, description=book.description)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def put_book(db: Session, db_book: models.book.BookDB):
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, db_book: models.book.BookDB) -> None:
    db.delete(db_book)
    db.commit()


def get_author(db: Session, author_id: int) -> AuthorDB:
    return db.query(AuthorDB).filter(AuthorDB.id == author_id).first()


def get_all_authors(db: Session, skip: int = 0, limit: int = 100):
    r = db.query(AuthorDB).offset(skip).limit(limit).all()
    # for i in r:
    #     print(i)
    return r


def create_author(db: Session, author: models.author.AuthorGetResponse) -> models.author.AuthorDB:
    db_author = AuthorDB(name=author.name, surname=author.surname,
                         age=author.age, language=author.language,
                         rating=author.rating)
    print(db_author)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def delete_author(db: Session, db_author: models.author.AuthorDB) -> None:
    db.delete(db_author)
    db.commit()


def put_author(db: Session, db_author: models.author.AuthorDB) -> models.author.AuthorDB:
    db.commit()
    db.refresh(db_author)
    return db_author
