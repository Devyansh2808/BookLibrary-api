from pydantic import BaseModel
import datetime
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_date: datetime.date
    isbn: str
    pages: int
    country: Optional[str] = None

class StoreBook(Book):
    id: int
    recieved_date: datetime.date
    count: int
