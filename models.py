from pydantic import BaseModel
import datetime
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_date: datetime.date
    isbn: str
    pages: int
    country: Optional[str] = None
    count: int = 1

class BookItem(BookCreate):
    id: int
    recieved_date: datetime.date
