from fastapi import APIRouter
from models.book import Book, PutBook
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

import crud
import models.author
from database import get_db

book_router = APIRouter(
    prefix="/book",
    tags=["book"],
)


@book_router.get("/{book_id}")
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        return {"message": "Book with id doesnt exist in db"}
    return db_book


@book_router.post("/")
def create_book(book: models.book.Book, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@book_router.get("/")
def all_books(db: Session = Depends(get_db)):
    all_books = crud.get_all_books(db)
    return {"Books": all_books}


@book_router.delete("/{book_id}")
def del_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        return {"message": f"Book with id {book_id} doesnt exist in db"}
    else:
        crud.delete_book(db, db_book)
        return {"Message": f"book with id {book_id} was deleted"}


@book_router.put("/")
def put_book_by_id(put_book: PutBook, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, put_book.id)
    if not db_book:
        return {"message": f"Book with id {put_book.id} doesnt exist in db"}
    db_book.book_name = put_book.book_name
    db_book.author_name = put_book.author_name
    db_book.rating = put_book.rating
    db_book.description = put_book.description
    updated_book = crud.put_book(db, db_book)
    return updated_book
#
#
# @router.patch("/{book_id}")
# def patch_book_by_id(patch_book: PatchBook, book_id: int):
#     if book_id not in fake_db:
#         return {"Message": "Book doesn't exist in the library"}
#     fake_db[book_id].author_name = patch_book.author_name if patch_book.author_name else fake_db[book_id].author_name
#     fake_db[book_id].book_name = patch_book.book_name if patch_book.book_name else fake_db[book_id].book_name
#     fake_db[book_id].rating = patch_book.rating if patch_book.rating else fake_db[book_id].rating
#     fake_db[book_id].description = patch_book.description if patch_book.description else fake_db[book_id].description
#     return {"Message": f"Book with id {book_id} was changed"}
