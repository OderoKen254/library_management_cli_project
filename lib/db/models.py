#Data models and validation logic

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from database import Base
import re
from datetime import datetime

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    publication_year = Column(Integer, nullable=False)
    borrower_id = Column(Integer, ForeignKey("borrowers.id"), nullable=True)

    #relationship
    borrower = relationship("Borrower", back_populates="books")

    #validators
    @validates('title', 'author')
    def validate_non_empty(self, key, value):
        if not value or value.strip() == '':
            raise ValueError(f"{key} cannot be empty")
        return value
    
    @validates('publication_year')
    def validate_publication_year(self, key, year):
        current_year = datetime.now().year
        if not (1800 <= year <= current_year):
            raise ValueError(f"Publication year must be between 1800 and {current_year}")
        return year
    
    @validates('isbn')
    def validate_isbn(self, key, isbn):
        if not re.match(r'^\d{10}|\d{13}$', isbn):
            raise ValueError("ISBN must be 10 or 13 digits"):
        elif not isbn.strip():
            raise ValueError("ISBN cannot be empty")
        return isbn



class Borrower(Base):
    __tablename__ = 'borrowers'
    pass


