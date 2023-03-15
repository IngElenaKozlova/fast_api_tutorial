from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

import crud
import models.author
from database import get_db

author_router = APIRouter(
    prefix="/author",
    tags=["author"],
)


@author_router.post("/")
def create_author(author: models.author.Author, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@author_router.get("/{author_id}")
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if not db_author:
        return {"message": "Author with id doesnt exist in db"}
    return db_author


@author_router.get("/")
def all_authors(db: Session = Depends(get_db)):
    all_authors = crud.get_all_authors(db)
    return {"Authors": all_authors}


@author_router.delete("/{author_id}")
def del_author_by_id(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if not db_author:
        return {"message": f"Author with id {author_id} doesnt exist in db"}
    else:
        crud.delete_author(db, db_author)
        return {"Message": f"Author with id {author_id} was deleted"}


@author_router.put("/")
def put_book_by_id(put_author: models.author.PutAuthor, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, put_author.id)
    if not db_author:
        return {"message": f"Book with id {put_author.id} doesnt exist in db"}
    db_author.name = put_author.name
    db_author.surname = put_author.surname
    db_author.rating = put_author.rating
    db_author.age = put_author.age
    db_author.language = put_author.language

    updated_author = crud.put_author(db, db_author)
    return updated_author


@author_router.patch("/")
def patch_author_by_id(patch_author: models.author.PatchAuthor, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, patch_author.id)
    if not db_author:
        return {"message": f"Book with id {patch_author.id} doesnt exist in db"}

    db_author.name = patch_author.name if patch_author.name else db_author.name
    db_author.surname = patch_author.surname if patch_author.surname else db_author.surname
    db_author.age = patch_author.age if patch_author.age else db_author.age
    db_author.language = patch_author.language if patch_author.language else db_author.language
    db_author.rating = patch_author.rating if patch_author.rating else db_author.rating

    updated_author = crud.put_author(db, db_author)
    return updated_author
