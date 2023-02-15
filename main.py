from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

import models.book
from database import engine, SessionLocal
from routers import book
from pydantic import BaseModel
import sql_book
import crud

app = FastAPI()

# app.include_router(book.router)

fake_db_authors = {}

sql_book.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/book")
def create_book(book: models.book.Book, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@app.get("/book/{book_id}")
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if not db_book:
        return {"message": "book with id doesnt exist in db"}
    return db_book

# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users

# class Author(BaseModel):
#     id: int
#     name_author: str
#     surname_author: str
#     age_author: int
#     language_author: str
#     rating_author: float
#
#
# @app.get("/author")
# def all_authors():
#     all_authors = [fake_db_authors[key] for key in fake_db_authors.keys()]
#     return {"Authors": all_authors}
#
#
# @app.get("/author/{author_id}")
# def one_author(author_id: int):
#     if author_id in fake_db_authors:
#         return {"Author": fake_db_authors[author_id]}
#     else:
#         return {"Message": "Author doesn't exist in the library"}
#
#
# @app.post("/author")
# def add_author(author: Author):
#     if author.id not in fake_db_authors:
#         fake_db_authors[author.id] = author
#     else:
#         return {"Message": f"Author with id {author.id} has already added to the library"}
#
#
# @app.delete("/author/{author_id}")
# def del_author_by_id(author_id: int):
#     if author_id in fake_db_authors:
#         del fake_db_authors[author_id]
#         return {"Message": "Author was successfully deleted"}
#     else:
#         return {"Message": "Author doesn't exist in the library"}
#
#
# @app.put("/author/{author_id}")
# def put_author_by_id(author: Author, author_id: int):
#     if author_id not in fake_db_authors:
#         return {"Message": "Author doesn't exist in the library"}
#     fake_db_authors[author_id] = author
#     return {"Message": f"Author with id {author_id} was changed"}
