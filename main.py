from fastapi import Depends, FastAPI, HTTPException
from models import *
import datetime
from database import Base, engine, SessionLocal
from database_models import Book
from sqlalchemy.orm import Session

app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.post("/books")
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_item = Book(
        **book.model_dump(),
        recieved_date=datetime.date.today(),
    )
    db.add(book_item)
    db.commit()
    db.refresh(book_item)
    return book_item

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.get("/books")
def read_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    existing_book = db.query(Book).filter(Book.id == book_id).first()
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.description = book.description
    existing_book.published_date = book.published_date
    existing_book.isbn = book.isbn
    existing_book.pages = book.pages
    existing_book.country = book.country
    db.commit()
    db.refresh(existing_book)
    return existing_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return book
