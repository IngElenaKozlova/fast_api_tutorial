from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

fake_db = {}

class Book(BaseModel):
    id: int
    author_name: str
    book_name: str
    rating: float
    description: str

@app.get("/book")
def all_books():
    all_books = [fake_db[key] for key in fake_db.keys()]
    return {"Books": all_books}


@app.get("/book/{book_id}")
def one_book(book_id: int):
    if book_id in fake_db:
        return {"Book": fake_db[book_id]}
    else:
        return {"Message": "Book doesn't exist in the library"}



@app.post("/book")
def add_book(book: Book):
    fake_db[book.id] = book
    return {"Message": "Book was saved to DB"}



@app.delete("/book/{book_id}")
def del_book_by_id(book_id: int):
    if book_id in fake_db:
        del fake_db[book_id]
        return {"Message": "Book was successfully deleted"}
    else:
        return {"Message": "Book doesn't exist in the library"}


