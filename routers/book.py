from fastapi import APIRouter

from models.book import Book, PatchBook

router = APIRouter(
    prefix="/book",
    tags=["book"],
)

fake_db = {}


@router.get("/")
def all_books():
    all_books = [fake_db[key] for key in fake_db.keys()]
    return {"Books": all_books}


@router.get("/{book_id}")
def one_book(book_id: int):
    if book_id in fake_db:
        return {"Book": fake_db[book_id]}
    else:
        return {"Message": "Book doesn't exist in the library"}


@router.post("/")
def add_book(book: Book):
    if book.id in fake_db:
        return {"Message": "Book has already saved to DB, add another book"}
    else:
        fake_db[book.id] = book
        return {"Message": "Book was saved to DB"}


@router.delete("/{book_id}")
def del_book_by_id(book_id: int):
    if book_id in fake_db:
        del fake_db[book_id]
        return {"Message": "Book was successfully deleted"}
    else:
        return {"Message": "Book doesn't exist in the library"}


@router.put("/{book_id}")
def put_book_by_id(book: Book, book_id: int):
    if book_id not in fake_db:
        return {"Message": "Book doesn't exist in the library"}
    fake_db[book_id] = book
    return {"Message": f"Book with id {book_id} was changed"}


@router.patch("/{book_id}")
def patch_book_by_id(patch_book: PatchBook, book_id: int):
    if book_id not in fake_db:
        return {"Message": "Book doesn't exist in the library"}
    fake_db[book_id].author_name = patch_book.author_name if patch_book.author_name else fake_db[book_id].author_name
    fake_db[book_id].book_name = patch_book.book_name if patch_book.book_name else fake_db[book_id].book_name
    fake_db[book_id].rating = patch_book.rating if patch_book.rating else fake_db[book_id].rating
    fake_db[book_id].description = patch_book.description if patch_book.description else fake_db[book_id].description
    return {"Message": f"Book with id {book_id} was changed"}
