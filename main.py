from fastapi import FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

import crud
import models.book
import models.author
from sql_models import sql_author, sql_book
from database import engine, SessionLocal

app = FastAPI()

# app.include_router(book.router)
# app.include_router(author.router)

sql_book.Base.metadata.create_all(bind=engine)

sql_author.Base.metadata.create_all(bind=engine)


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
        return {"message": "Book with id doesnt exist in db"}
    return db_book


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


@app.post("/author")
def create_author(author: models.author.Author, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@app.get("/author/{author_id}")
def get_author_by_id(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if not db_author:
        return {"message": "Author with id doesnt exist in db"}
    return db_author
