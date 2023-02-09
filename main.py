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


class PatchBook(BaseModel):
    author_name: str | None
    book_name: str | None
    rating: float | None
    description: str | None


@app.get("/")
def hello_page():
    return {"message": "Hello from Fast API"}


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
    if book.id in fake_db:
        return {"Message": "Book has already saved to DB, add another book"}
    else:
        fake_db[book.id] = book
        return {"Message": "Book was saved to DB"}



@app.delete("/book/{book_id}")
def del_book_by_id(book_id: int):
    if book_id in fake_db:
        del fake_db[book_id]
        return {"Message": "Book was successfully deleted"}
    else:
        return {"Message": "Book doesn't exist in the library"}


@app.put("/book/{book_id}")
def put_book_by_id(book: Book, book_id: int):
    if book_id not in fake_db:
        return {"Message": "Book doesn't exist in the library"}
    fake_db[book_id] = book
    return {"Message": f"Book with id {book_id} was changed"}


@app.patch("/book/{book_id}")
def patch_book_by_id(patch_book: PatchBook, book_id: int):
    if book_id not in fake_db:
        return {"Message": "Book doesn't exist in the library"}
    fake_db[book_id].author_name = patch_book.author_name if patch_book.author_name else fake_db[book_id].author_name
    fake_db[book_id].book_name = patch_book.book_name if patch_book.book_name else fake_db[book_id].book_name
    fake_db[book_id].rating = patch_book.rating if patch_book.rating else fake_db[book_id].rating
    fake_db[book_id].description = patch_book.description if patch_book.description else fake_db[book_id].description
    return {"Message": f"Book with id {book_id} was changed"}

# Автор: id, name, surname, age, language, rating
# Организовать методы GET_all, GET by id, POST, PUT, DELETE для авторов

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

# @app.post("/author")
# def add_author(author: Author):
#     fake_db_authors[author.id] = author
#     return {"Message": "Author was saved to DB"}

@app.post("/author")
def add_author(author: Author):
    if author.id not in fake_db_authors:
        fake_db_authors[author.id] = author
    else:
        return {"Message": f"Author with id {author.id} has already added to the library"}

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

