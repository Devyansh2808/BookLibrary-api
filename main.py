from fastapi import FastAPI, HTTPException
from models import *
import datetime

books_db = {}
next_id = 1


app = FastAPI()
#es
@app.post("/books")
def create_book(book: BookCreate):
    global next_id
    book_item = BookItem(
        id=next_id,
        title=book.title,
        author=book.author,
        description=book.description,
        published_date=book.published_date,
        isbn=book.isbn,
        pages=book.pages,
        country=book.country,
        recieved_date=datetime.date.today(),
        count=1
    )
    books_db[next_id] = book_item
    next_id += 1
    return book_item

@app.get("/books/{book_id}")
def read_book(book_id: int):
    book = books_db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.get("/books")
def read_books():
    return list(books_db.values())

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    existing_book = books_db.get(book_id)
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    updated_book = BookItem(
        id=book_id,
        title=book.title,
        author=book.author,
        description=book.description,
        published_date=book.published_date,
        isbn=book.isbn,
        pages=book.pages,
        country=book.country,
        recieved_date=existing_book.recieved_date,
        count=existing_book.count
    )
    books_db[book_id] = updated_book
    return updated_book
