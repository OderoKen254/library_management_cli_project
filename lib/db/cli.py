#CLI Interface and Menu Logic

from database import Session
from model import Book, Borrower
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