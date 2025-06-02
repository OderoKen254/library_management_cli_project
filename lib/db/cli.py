#CLI Interface and Menu Logic

from database import Session
from model import Book, Borrower
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

def main_menu():
    while True:
        print("\n****Library Management System****")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. View All Books")
        print("4. Search Book")
        print("5. Back to Main Menu")
        print("6. Exit")
        
        choice = input("Select an option (1-5): ")
        if choice == '1':
            add_book()
        elif choice == '2':
            delete_book()
        elif choice == '3':
            view_books()
        elif choice == '4':
            search_book()
        elif choice == '5':
            main_menu()
        elif choice == '6':
            print("Exiting Books Menu")
            break
        else:
            print("Invalid choice. Please try again")