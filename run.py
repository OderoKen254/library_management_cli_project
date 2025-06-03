#Main Entry Point
from lib.cli import CLI

def main():
    cli = CLI()
    cli.main_menu()

if __name__ == "__main__":
    main()

# from lib.cli import LibraryCLI

# def main():
#     cli = LibraryCLI()
#     cli.main_menu()

# if __name__ == "__main__":
#     main()

# def main():
#     """Initialize database and start CLI."""
#     init_db()
#     cli = LibraryCLI()
#     cli.main_menu()

# if __name__ == "__main__":
#     main()