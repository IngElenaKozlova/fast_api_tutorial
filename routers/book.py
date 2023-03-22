from fastapi import APIRouter
from models.book import PutBook, PostBookResponse
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

import crud
import models.author
from database import get_db

book_router = APIRouter(
    prefix="/book",
    tags=["book"],
)


@book_router.get("/", response_model=list[PostBookResponse])
def all_books(db: Session = Depends(get_db)):
    all_books = crud.get_all_books(db)
    return all_books


@book_router.get("/{book_id}", response_model=PostBookResponse)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        return {"message": "Book with id doesnt exist in db"}
    return db_book


@book_router.post("/", response_model=PostBookResponse)
def create_book(book: models.book.PostBook, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@book_router.delete("/{book_id}")
def del_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        return {"message": f"Book with id {book_id} doesnt exist in db"}
    else:
        crud.delete_book(db, db_book)
        return {"Message": f"book with id {book_id} was deleted"}


@book_router.put("/", response_model=PostBookResponse)
def put_book_by_id(put_book: PutBook, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, put_book.id)
    if not db_book:
        return {"message": f"Book with id {put_book.id} doesnt exist in db"}
    db_book.book_name = put_book.book_name
    db_book.author_id = put_book.author_id
    db_book.rating = put_book.rating
    db_book.description = put_book.description
    updated_book = crud.put_book(db, db_book)
    return updated_book
