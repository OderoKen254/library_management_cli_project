#Data models and validation logic

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from database import Base
import re
from datetime import datetime

class Book(Base):
    __tablename__ = "books"
    pass



class Borrower(Base):
    __tablename__ = 'borrowers'
    pass


