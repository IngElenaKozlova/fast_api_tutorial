from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

fake_db = {}


# GET (Запрос) POST (отправка данных на сервер) # PUT (изменение уже существующих данных на сервере (полные данные))
# PATСH (изменение уже существующих данных на сервере (кусок данных)) DELETE (удаляем данные)
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
    # [Book("id"=1, "author_name"="First Author", "book_name"="Test Book", "rating"=1.1, "description"="rfrfrfmrkfm")]
    return {"Books": all_books}


# что здесь конкретно является ключом в fake_db[key] ? для ключей в словаре мы создаем ключи, а значениями являются все
# книги иначе вся инфа, которую мы введём ?

@app.get("/book/{book_id}")
def one_book(book_id: int):
    if book_id in fake_db:
        return {"Book": fake_db[book_id]}
    else:
        return {"Message": "Book doesn't exist in the library"}


# что такое book_id в этом случае ? созданный "путь" с чисельным названием, который мы просто определили и почему
# получается, что он как бы содержит внутри информацию о книге? - потому что это ключ. Но как мы определили, что он
# содержит информацию о книге ? - мы вводим инфо сами в постмане, то есть value в прямом смысле задается нами потом?
# и почему он в фигурных скобках? и почему тогда
# в return мы возвращем просто {"Book": fake_db[book_id]}, а не {"Book id": fake_db[book_id]}, так бы было понятнее


# @app.post("/book")
# def add_book(book: Book):
#     fake_db[book.id] = book
#     return {"Message": "Book was saved to DB"}

# домашка: изменить метод пост с тем, что если ид уже существует, то высветить мессадж об этом, а если не сущ то адд
# что такое .id ? атрибут экземпляра book класса Book ? то есть новая пара ключ-значение создается по ключу, которым
# является атрибут класса и так создается одновременно и новый id ?

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

