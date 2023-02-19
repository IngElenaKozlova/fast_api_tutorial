from fastapi import APIRouter

from models.author import Author, PatchAuthor

router = APIRouter(
    prefix="/author",
    tags=["author"],
)

fake_db_authors = {}


@router.get("/")
def all_authors():
    all_authors = [fake_db_authors[key] for key in fake_db_authors.keys()]
    return {"Authors": all_authors}


@router.get("/{author_id}")
def one_author(author_id: int):
    if author_id in fake_db_authors:
        return {"Author": fake_db_authors[author_id]}
    else:
        return {"Message": "Author doesn't exist in the library"}


@router.post("/")
def add_author(author: Author):
    if author.id not in fake_db_authors:
        fake_db_authors[author.id] = author
    else:
        return {"Message": f"Author with id {author.id} has already added to the library"}


@router.delete("/{author_id}")
def del_author_by_id(author_id: int):
    if author_id in fake_db_authors:
        del fake_db_authors[author_id]
        return {"Message": "Author was successfully deleted"}
    else:
        return {"Message": "Author doesn't exist in the library"}


@router.put("/{author_id}")
def put_author_by_id(author: Author, author_id: int):
    if author_id not in fake_db_authors:
        return {"Message": "Author doesn't exist in the library"}
    fake_db_authors[author_id] = author
    return {"Message": f"Author with id {author_id} was changed"}


@router.patch("/{author_id}")
def patch_author_by_id(patch_author: PatchAuthor, author_id: int):
    if author_id not in fake_db_authors:
        return {"Message": "Book doesn't exist in the library"}
    fake_db_authors[author_id].name_author = patch_author.name_author if patch_author.name_author else fake_db_authors[
        author_id].name_author
    fake_db_authors[author_id].surname_author = patch_author.surname_author if patch_author.surname_author else \
        fake_db_authors[author_id].surname_author
    fake_db_authors[author_id].age_author = patch_author.age_author if patch_author.age_author else fake_db_authors[
        author_id].age_author
    fake_db_authors[author_id].language_author = patch_author.language_author if patch_author.language_author else \
        fake_db_authors[author_id].language_author
    fake_db_authors[author_id].rating_author = patch_author.rating_author if patch_author.rating_author else \
        fake_db_authors[author_id].rating_author
    return {"Message": f"Author with id {author_id} was changed"}
