from fastapi import APIRouter, status, HTTPException
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


@book_router.get("/", response_model=list[PostBookResponse], status_code=status.HTTP_200_OK)
def all_books(db: Session = Depends(get_db)):
    all_books = crud.get_all_books(db)
    return all_books


@book_router.get("/{book_id}", response_model=PostBookResponse, status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {book_id} doesn't exist in db")
    return db_book


@book_router.post("/", response_model=PostBookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: models.book.PostBook, db: Session = Depends(get_db)):
    """
       Create a book record in db:

       - **book name**: each item must have a name
       - **rating**: each item must have a rating
       - **description**: a long description
       """
    return crud.create_book(db=db, book=book)


@book_router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def del_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {book_id} doesn't exist in db")
    else:
        crud.delete_book(db, db_book)
        return {"Message": f"book with id {book_id} was deleted"}


@book_router.put("/", response_model=PostBookResponse, status_code=status.HTTP_200_OK)
def put_book_by_id(put_book: PutBook, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, put_book.id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {put_book.id} doesn't exist in db")
    db_book.book_name = put_book.book_name
    db_book.author_id = put_book.author_id
    db_book.rating = put_book.rating
    db_book.description = put_book.description
    updated_book = crud.put_book(db, db_book)
    return updated_book


@book_router.patch("/", response_model=PostBookResponse, status_code=status.HTTP_200_OK)
def patch_book_by_id(patch_book: models.book.PatchBook, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, patch_book.id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with id {patch_book.id} doesn't exist in db")

    db_book.author_id = patch_book.author_id if patch_book.author_id else db_book.author_id
    db_book.book_name = patch_book.book_name if patch_book.book_name else db_book.book_name
    db_book.rating = patch_book.rating if patch_book.rating else db_book.rating
    db_book.description = patch_book.description if patch_book.description else db_book.description

    updated_book = crud.put_author(db, db_book)
    return updated_book
