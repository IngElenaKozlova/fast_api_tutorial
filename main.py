from fastapi import FastAPI
import models.book
import models.author
from database import engine
from routers.author import author_router
from routers.book import book_router

app = FastAPI()

app.include_router(book_router)
app.include_router(author_router)

models.book.Base.metadata.create_all(bind=engine)

models.author.Base.metadata.create_all(bind=engine)

# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
