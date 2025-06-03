CLI project:
Desc.
This Library Management CLI Application is a Python-based command-line tool for managing a library’s books and borrowers. It uses SQLAlchemy with a SQLite database to store data persistently. Users can create, delete, view, and search books and borrowers, and track borrowing relationships (one borrower can borrow multiple books). The application features a menu-driven interface with input validation, following OOP best practices and modular code organization.

MVPs
1. Database Setup: SQLite database with two tables: Book (id, title, author, isbn, publication_year, borrower_id) and Borrower (id, name, email, phone).
One-to-many relationship: Book.borrower_id links to Borrower.id.
Property methods to validate: unique ISBN, valid email format, non-empty fields, realistic publication year.

2. CLI Menu Interface: Main menu with options for managing books, borrowers, or exiting.
Sub-menus for each model with options to:
   Create a new book or borrower.
   Delete a book or borrower by ID.
   Display all books or borrowers.
   View books borrowed by a specific borrower.
   Find a book by title or ISBN, or a borrower by name or email.

3.Input Validation and Error Handling:
Validate inputs (e.g., unique ISBN, valid email, non-empty fields).
Provide clear error messages for invalid inputs or failed operations (e.g., deleting a non-existent book)

4. Project Organization



