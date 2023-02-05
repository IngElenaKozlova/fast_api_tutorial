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


fake_db_authors = {}

class Author(BaseModel):
    id: int
    name_author: str
    surname_author: str
    age_author: int
    language_author: str
    rating_author: float

@app.get("/author")
def all_authors():
    all_authors = [fake_db_authors[key] for key in fake_db_authors.keys()]
    return {"Authors": all_authors}

@app.get("/author/{author_id}")
def one_author(author_id: int):
    if author_id in fake_db_authors:
        return {"Author": fake_db_authors[author_id]}
    else:
        return {"Message": "Author doesn't exist in the library"}

@app.post("/author")
def add_author(author: Author):
    fake_db_authors[author.id] = author
    return {"Message": "Author was saved to DB"}

@app.delete("/author/{author_id}")
def del_author_by_id(author_id: int):
    if author_id in fake_db_authors:
        del fake_db_authors[author_id]
        return {"Message": "Author was successfully deleted"}
    else:
        return {"Message": "Author doesn't exist in the library"}

@app.put("/author/{author_id}")
def put_author_by_id(author: Author, author_id: int):
    if author_id not in fake_db_authors:
        return {"Message": "Author doesn't exist in the library"}
    fake_db_authors[author_id] = author
    return {"Message": f"Author with id {author_id} was changed"}

