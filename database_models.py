from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from database import Base

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String, nullable=True)
    published_date = Column(DateTime, nullable=False)
    isbn = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    country = Column(String, nullable=True)
    recieved_date = Column(DateTime, default=datetime.utcnow)