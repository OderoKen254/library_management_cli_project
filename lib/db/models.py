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
    issued = Column(DateTime, nullable=True)

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
    
    @validates('borrower_id')
    def validate_borrower_id(self, key, borrower_id):
        if borrower_id is not None:
            self.issued = datetime.now()
        else:
            self.issued = None
        return borrower_id
    
    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', issued={self.issued})>"



class Borrower(Base):
    __tablename__ = 'borrowers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)

    #Relationship
    books = relationship("Book", back_populates="borrower")

    #validators
    @validates('name')
    def validate_name(self, key, name):
        if not name or name.strip() == '':
            raise ValueError("Name cannot be empty")
        return name
    
    @validates('phone')
    def validate_phone(self, key, phone):
        if phone and not re.match(r'^\+?\d{10,15}$', phone):
            raise ValueError("Invalid phone number format")
        return phone
    
    @validates('email')
    def validate_email(self, key, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Invalid email format")
        return email
    

    def __repr__(self):
        return f"<Borrower(name='{self.name}', email='{self.email}')>"


