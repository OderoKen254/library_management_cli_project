#Main Entry Point

from database import init_db
from lib.cli import LibraryCLI

def main():
    """Initialize database and start CLI."""
    init_db()
    cli = LibraryCLI()
    cli.main_menu()

if __name__ == "__main__":
    main()