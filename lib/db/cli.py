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
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def book_menu():
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


def add_book(session):
    try:
        title = input("Enter book title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        year = int(input("Enter publication year: "))
        borrower_id = input("Enter borrower ID (leave blank if none): ")
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
    try:
        book_id = int(input("Enter book ID to delete: "))
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
    books = session.query(Book).all()
    if books:
        for book in books:
            borrower = book.borrower.name if book.borrower else "None"
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Year: {book.publication_year}, Borrower: {borrower}")
    else:
        print("No books found.")

def find_book(session):
    search = input("Enter title or ISBN to search: ")
    books = session.query(Book).filter((Book.title.ilike(f"%{search}%")) | (Book.isbn == search)).all()
    if books:
        for book in books:
            borrower = book.borrower.name if book.borrower else "None"
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Year: {book.publication_year}, Borrower: {borrower}")
    else:
        print("No books found.")


def view_borrowed_books(session):
    try:
        borrower_id = int(input("Enter borrower ID: "))
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


def add_borrower(session):
    try:
        name = input("Enter borrower name: ")
        email = input("Enter email: ")
        phone = input("Enter phone (optional): ") or None
        borrower = Borrower(name=name, email=email, phone=phone)
        session.add(borrower)
        session.commit()
        print("Borrower added successfully!")
    except (ValueError, IntegrityError) as e:
        session.rollback()
        print(f"Error: {str(e)}")


def delete_borrower(session):
    try:
        borrower_id = int(input("Enter borrower ID to delete: "))
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
    borrowers = session.query(Borrower).all()
    if borrowers:
        for borrower in borrowers:
            print(f"ID: {borrower.id}, Name: {borrower.name}, Email: {borrower.email}, Phone: {borrower.phone or 'None'}")
    else:
        print("No borrowers found.")


def find_borrower(session):
    search = input("Enter name or email to search: ")
    borrowers = session.query(Borrower).filter((Borrower.name.ilike(f"%{search}%")) | (Borrower.email == search)).all()
    if borrowers:
        for borrower in borrowers:
            print(f"ID: {borrower.id}, Name: {borrower.name}, Email: {borrower.email}, Phone: {borrower.phone or 'None'}")
    else:
        print("No borrowers found.")