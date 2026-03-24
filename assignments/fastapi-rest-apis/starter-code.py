from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BookIn(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": 2, "title": "Clean Architecture", "author": "Robert C. Martin", "year": 2017},
    {"id": 3, "title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015},
]


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/books")
def list_books() -> list[dict]:
    return books


@app.post("/books", status_code=201)
def create_book(payload: BookIn) -> dict:
    new_book = {
        "id": len(books) + 1,
        "title": payload.title,
        "author": payload.author,
        "year": payload.year,
    }
    books.append(new_book)
    return new_book
