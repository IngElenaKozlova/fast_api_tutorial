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


@app.post("/book")
def add_book(book: Book):
    fake_db[book.id] = book
    return {"Message": "Book was saved to DB"}

# домашка: изменить метод пост с тем, что если ид уже существует, то высветить мессадж об этом, а если не сущ то адд
# что такое .id ? атрибут экземпляра book класса Book ? то есть новая пара ключ-значение создается по ключу, которым
# является атрибут класса и так создается одновременно и новый id ?

# @app.post("/book")
# def add_book(book: Book):
#     if book in fake_db:
#         return {"Message": "Book has already saved to DB, add another book"}
#     else:
#         fake_db[book.id] = book
#         return {"Message": "Book was saved to DB"}


@app.delete("/book/{book_id}")
def del_book_by_id(book_id: int):
    if book_id in fake_db:
        del fake_db[book_id]
        return {"Message": "Book was successfully deleted"}
    else:
        return {"Message": "Book doesn't exist in the library"}

# если book_id это созданный "путь" с чисельным названием, который мы просто определили, то почему при его удалении,
# удаляется и вся информация о книге ?

