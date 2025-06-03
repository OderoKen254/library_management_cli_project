from database import Base, Session, engine
from lib.db.models import Book, Borrower
from sqlalchemy.exc import IntegrityError
from datetime import datetime

def seed_data():
    # Clear existing data
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()
    try:
        # Create sample borrowers
        borrower1 = Borrower(
            name="Kennedy Rodgers",
            email="kenn.rodgers@example.com",
            phone="+12345678901"
        )
        borrower2 = Borrower(
            name="Bob Johnson",
            email="bob.johnson@example.com",
            phone="+12345678902"
        )
        borrower3 = Borrower(
            name="Carol Williams",
            email="carol.williams@example.com",
            phone="+12345678903"
        )
        borrower4 = Borrower(
            name="David Brown",
            email="david.brown@example.com",
            phone="+12345678904"
        )
        borrower5 = Borrower(
            name="Emma Morgan",
            email="emma.morgan@example.com",
            phone="+12345678905"
        )
        session.add_all([borrower1, borrower2, borrower3, borrower4, borrower5])
        session.commit()

        # Create sample books
        book1 = Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            isbn="9780743273565",
            publication_year=1925,
            borrower_id=borrower1.id
        )
        book2 = Book(
            title="To Kill a Mockingbird",
            author="Harper Lee",
            isbn="9780446310789",
            publication_year=1960
        )
        book3 = Book(
            title="1984",
            author="George Orwell",
            isbn="9780451524935",
            publication_year=1949,
            borrower_id=borrower2.id
        )
        book4 = Book(
            title="Pride and Prejudice",
            author="Jane Austen",
            isbn="9780141439518",
            publication_year=1813
        )
        book5 = Book(
            title="The Catcher in the Rye",
            author="J.D. Salinger",
            isbn="9780316769488",
            publication_year=1951,
            borrower_id=borrower1.id
        )
        book6 = Book(
            title="Brave New World",
            author="Aldous Huxley",
            isbn="9780060850524",
            publication_year=1932,
            borrower_id=borrower3.id
        )
        book7 = Book(
            title="Jane Eyre",
            author="Charlotte Brontë",
            isbn="9780141441146",
            publication_year=1847
        )
        book8 = Book(
            title="Lord of the Flies",
            author="William Golding",
            isbn="9780399501487",
            publication_year=1954
        )
        session.add_all([book1, book2, book3, book4, book5, book6, book7, book8])
        session.commit()

        print("Database seeded successfully with 5 borrowers and 8 books.")
    except IntegrityError as e:
        session.rollback()
        print(f"Error: Failed to seed data due to integrity constraint violation: {str(e)}")
    except Exception as e:
        session.rollback()
        print(f"Error: Failed to seed data: {str(e)}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_data()