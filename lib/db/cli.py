#CLI Interface and Menu Logic

from database import Session
from models import Book, Borrower
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

def main_menu():
    while True:
        print("\n****Library Management System****")
        print("1. Manage Books")
        print("2. Manage Borrowers")
        print("3. Exit")

        choice = ("Select an option (1-3): ")
        if choice == '1':
            book_menu()
        elif choice == '2':
            borrower_menu()
        elif choice == '3':
            print("...Exiting library session. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def book_menu():
    """Display book management sub-menu."""
    session = Session()
    while True:
        print("\n......Book Management.......")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. View All Books")
        print("4. View Borrowed Books")
        print("5. Find Book by Title or ISBN")
        print("6. Back to Main Menu")
        
        choice = input("Select an option (1-6): ")
        if choice == '1':
            add_book(session)
        elif choice == '2':
            delete_book(session)
        elif choice == '3':
            view_all_books(session)
        elif choice == '4':
            view_borrowed_book(session)
        elif choice == '5':
            find_books(session)
        elif choice == '6':
            print("Exiting Books Menu")
            break
        else:
            print("Invalid choice entry. Please try again.")
    session.close()


def borrower_menu():
    """Display borrower management sub-menu."""
    session = Session()
    while True:
        print("\n======Borrower Management======")
        print("1. Add Borrower")
        print("2. Delete Borrower")
        print("3. View All Borrowers")
        print("4. Find Borrower by Name or Email")
        print("5. Back")

        choice = input("Select any options (1-5): ")
        if choice == '1':
            add_borrower(session)
        elif choice == '2':
            delete_borrower(session)
        elif choice == '3':
            view_all_borrowers(session)
        elif choice == '4':
            find_borrower(session)
        elif choice == '5':
            break
        else:
            print("Invalid choice entry. Please try again.")
    session.close()


# Book handling functions
def add_book(session):
    """Add a new book with validation."""
    try:
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        year = int(input("Publication year: "))
        borrower_id = input("Borrower ID (leave blank if none): ")
        borrower_id = int(borrower_id) if borrower_id else None
        if borrower_id:
            borrower = session.query(Borrower).get(borrower_id)
            if not borrower:
                print("Borrower not found!")
                return
        book = Book(title=title, author=author, isbn=isbn, publication_year=year, borrower_id=borrower_id)
        session.add(book)
        session.commit()
        print("Book added successfully!")
    except (ValueError, IntegrityError) as e:
        session.rollback()
        print(f"Error: {str(e)}")


def delete_book(session):
    """Delete a book by ID."""
    try:
        book_id = int(input("Book ID to delete: "))
        book = session.query(Book).get(book_id)
        if book:
            session.delete(book)
            session.commit()
            print("Book deleted successfully!")
        else:
            print("Book not found!")
    except ValueError as e:
        print(f"Error: {str(e)}")


def view_all_books(session):
    """Display all books."""
    books = session.query(Book).all()
    if books:
        for book in books:
            borrower = book.borrower.name if book.borrower else "None"
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Year: {book.publication_year}, Borrower: {borrower}")
    else:
        print("No books found.")

def find_book(session):
    """Find a book by title or ISBN."""
    search = input("Enter title or ISBN: ")
    books = session.query(Book).filter((Book.title.ilike(f"%{search}%")) | (Book.isbn == search)).all()
    if books:
        for book in books:
            borrower = book.borrower.name if book.borrower else "None"
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Year: {book.publication_year}, Borrower: {borrower}")
    else:
        print("No books found.")


def view_borrowed_books(session):
    """View books borrowed by a specific borrower."""
    try:
        borrower_id = int(input("Borrower ID: "))
        borrower = session.query(Borrower).get(borrower_id)
        if borrower:
            books = session.query(Book).filter(Book.borrower_id == borrower_id).all()
            if books:
                print(f"Books borrowed by {borrower.name}:")
                for book in books:
                    print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Year: {book.publication_year}")
            else:
                print("No books borrowed by this borrower.")
        else:
            print("Borrower not found!")
    except ValueError as e:
        print(f"Error: {str(e)}")


#Borrower/user handling functions
def add_borrower(session):
    """Add a new borrower with validation."""
    try:
        name = input("Borrower name: ")
        email = input("Email: ")
        phone = input("Phone (optional): ") or None
        borrower = Borrower(name=name, email=email, phone=phone)
        session.add(borrower)
        session.commit()
        print("Borrower added successfully!")
    except (ValueError, IntegrityError) as e:
        session.rollback()
        print(f"Error: {str(e)}")


def delete_borrower(session):
    """Delete a borrower by ID."""
    try:
        borrower_id = int(input("Borrower ID to delete: "))
        borrower = session.query(Borrower).get(borrower_id)
        if borrower:
            if borrower.books:
                print("Cannot delete borrower with active loans!")
                return
            session.delete(borrower)
            session.commit()
            print("Borrower deleted successfully!")
        else:
            print("Borrower not found!")
    except ValueError as e:
        print(f"Error: {str(e)}")


def view_all_borrowers(session):
    """Display all borrowers."""
    borrowers = session.query(Borrower).all()
    if borrowers:
        for borrower in borrowers:
            print(f"ID: {borrower.id}, Name: {borrower.name}, Email: {borrower.email}, Phone: {borrower.phone or 'None'}")
    else:
        print("No borrowers found.")


def find_borrower(session):
    """Find a borrower by name or email."""
    search = input("Name or email: ")
    borrowers = session.query(Borrower).filter((Borrower.name.ilike(f"%{search}%")) | (Borrower.email == search)).all()
    if borrowers:
        for borrower in borrowers:
            print(f"ID: {borrower.id}, Name: {borrower.name}, Email: {borrower.email}, Phone: {borrower.phone or 'None'}")
    else:
        print("No borrowers found.")