
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # geçici olarak herkes erişebilir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# database.json dosyasını backend klasöründe tut
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOKS_FILE = os.path.join(BASE_DIR, "database.json")

# İlk başta dosya yoksa oluştur
if not os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

# Veri modelleri
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class BookUpdate(BaseModel):
    title: str
    author: str
    year: int

# Yardımcı fonksiyonlar
def read_books() -> List[Book]:
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**item) for item in data]
    except json.JSONDecodeError:
        return []

def write_books(books: list[Book]):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump([book.dict() for book in books], f, indent=2)

# API Routes
@app.get("/books", response_model=List[Book])
def get_books():
    return read_books()

@app.post("/books", response_model=Book)
def add_book(book_data: BookCreate):
    books = read_books()
    new_id = max([b.id for b in books], default=0) + 1
    new_book = Book(id=new_id, **book_data.dict())
    books.append(new_book)
    write_books(books)
    return new_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, update: BookUpdate):
    books = read_books()
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(id=book_id, **update.dict())
            books[index] = updated_book
            write_books(books)
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    books = read_books()
    new_books = [b for b in books if b.id != book_id]
    if len(books) == len(new_books):
        raise HTTPException(status_code=404, detail="Book not found")
    write_books(new_books)
    return {"message": "Book deleted"}
