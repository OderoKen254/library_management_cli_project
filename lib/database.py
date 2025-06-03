# Database setup and session management

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

#Sqlite db set up
DATABASE_URL = "sqlite:///library.db"
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def get_session():
    """Create and return a new database session."""
    return Session()

def init_db():
    """Initialize the database by creating tables."""
    try:
        Base.metadata.create_all(engine)
        print("Database initialized successfully.")
    except SQLAlchemyError as e:
        print(f"Error initializing database: {e}")

