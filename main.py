from fastapi import FastAPI, HTTPException
from models import *
import datetime

books_db = {}
next_id = 1


app = FastAPI()
@app.post("/books")
def create_book(book: BookCreate):
    global next_id
    book_item = BookItem(
        id=next_id,
        **book.model_dump(),
        recieved_date=datetime.date.today(),
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
        **book.model_dump(),
        id=book_id,
        recieved_date=existing_book.recieved_date,
        count=existing_book.count
    )
    books_db[book_id] = updated_book
    return updated_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db.pop(book_id)
