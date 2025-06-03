Library Management CLI Application

Overview
This is a Python-based command-line interface (CLI) application for managing a library's books and borrowers. It uses SQLAlchemy with a SQLite database to store data persistently. The application allows users to create, delete, view, and search books and borrowers, as well as track borrowing relationships (one borrower can borrow multiple books). The application features a menu-driven interface with input validation, adhering to object-oriented programming (OOP) best practices and modular code organization.

Features
- Database Management: SQLite database with two tables:
- Book: Stores book details (ID, title, author, ISBN, publication year, borrower ID).
- Borrower: Stores borrower details (ID, name, email, phone).
- One-to-many relationship: A borrower can borrow multiple books.
- Track which books are issued to which borrowers
- Clean CLI interface with input validation and error handling
- Persistent SQLite database

CLI Menu Interface:
Main menu with options to manage books, borrowers, or exit.
Sub-menus for creating, deleting, displaying, and searching books or borrowers.
View books borrowed by a specific borrower.
Search books by title or ISBN, and borrowers by name or email.
Input Validation: Ensures unique ISBNs, valid email formats, non-empty fields, and realistic publication years.
Error Handling: Provides clear error messages for invalid inputs or failed operations (e.g., deleting a non-existent book).
Modular Design: Organized into separate modules for data models, CLI logic, database setup, and main entry point.

Requirements
Python 3.8 or higher
SQLAlchemy (pip install sqlalchemy)

Installation
1. Clone or download the project repository:
git clone <repository-url>
cd library-management-cli

2. Create a virtual environment:
pipenv shell

3. Install the required dependencies:
pip install sqlalchemy

4. Ensure SQLite is available (it comes built-in with Python).


Usage

1. Run the application:
python run.py

2. Follow the menu prompts to:
Manage books (create, delete, view, search by title or ISBN).
Manage borrowers (create, delete, view, search by name or email).
View books borrowed by a specific borrower.
Exit the application.

3. Example menu:
Library Management System
1. Manage Books
2. Manage Borrowers
3. Exit
Enter choice:

Project Structure
CLI-LIBRARY-MANAGEMENT-PROJECT/
├── lib/
│   ├── __pycache__/                  # Compiled Python bytecode files
│   ├── db/
│   │   ├── __pycache__/              # Compiled bytecode for db module
│   │   ├── models.py                 # Book and Borrower data models (previously model.py)
│   │   └── seed.py                   # Script to seed the database with initial data
│   ├── .gitignore                    # Git ignore file
│   ├── cli.py                        # CLI logic and menu-driven interface
│   └── debug.py                      # Debugging utilities (optional)
├── migrations/                       # Alembic migrations for database schema changes
├── alembic.ini                       # Configuration file for Alembic migrations
├── database.db                       # SQLite database file
├── Pipfile                           # Pipenv dependency management file
├── Pipfile.lock                      # Lock file for Pipenv dependencies
├── README.md                         # Project documentation
└── run.py                            # Main entry point for the application



Notes
Make sure library.db is writable in your working directory.
Publication year must be between 1450 and the current year.
ISBNs and emails must be unique and valid.

License
MIT License: 
---

Let me know if you want a `setup.py` to go with it, or if you want me to generate a `.zip` of the whole project.

