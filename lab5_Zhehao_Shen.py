# Name: Zhehao Shen
# Student Number: 041145921
# Section: CST8279_010
# Date: 2025-06-09
# Description: Lab5_library Management System

# Define a Book class
class Book:
    # Initialize a Book object with title, author, ISBN, and available copies as an array.
    def __init__(self, title, author, isbn, available_copies):
        self.books = [title, author, isbn, available_copies]

    # Create function display_info() to show book details.
    def display_info(self):
        print(f"\n--- Book Information ---")
        print(f"Title: {self.books[0]}")
        print(f"Author: {self.books[1]}")
        print(f"ISBN: {self.books[2]}")
        print(f"Available_copies: {self.books[3]}")

    # Create function borrow_book() to borrow a book and update the number of available_copies.
    def borrow_book(self):
        if self.books[3] > 0:
            self.books[3] -= 1
            print(f"Successfully borrowed '{self.books[0]}'. Remaining copies: {self.books[3]}")
            return True
        else:
            print(f"Sorry, '{self.books[0]}' is currently out of stock.")
            return False

    # Create function return_book() to return a book and update the number of available_copies.
    def return_book(self):
        self.books[3] += 1
        print(f"Successfully returned '{self.books[0]}'. Available copies: {self.books[3]}")

# Define a Library class
class Library:
    # Initialize the library with an empty list of books.
    def __init__(self):
        self.books = []

    # Create function add_book() to add a new book.
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.books[0]}' has been added to the library.")

    # Create function find_book_by_title() to search for a book by title.
    def find_book_by_title(self, title):
        for book in self.books:
            if book.books[0].lower() == title.lower():
                return book
        return None

    # Create function display_all_books() to list all books in the library.
    def display_all_books(self):
        if self.books:
            print("\n=== Library Catalog ===")
            counter = 1
            for book in self.books:
                print(
                    f"{counter}. {book.books[0]} by {book.books[1]} (ISBN: {book.books[2]}) - {book.books[3]} copies available")
                counter += 1
        else:
            print("No books available in the library.")

# Create Main function to run the library management system.

# 2.Borrow and return books, and display their updated status.
# 3.Search for a book by title and display its details.
def main():
    library = Library()

    # 1.Create a few default books and add them to the library.
    sample_books = [
        Book("Harry Potter and the Sorcerer's Stone", "J. K. Rowling", "978-0-43-913316-6", 3),
        Book("The Red and the Black", "Stendhal", "978-0-81-297207-8", 2),
        Book("Lost Illusions", "Honoré de Balzac", "978-0-37-575790-7", 2)
    ]

    for book in sample_books:
        library.add_book(book)

    print("Welcome to the Library Management System.")

    while True:
        print("\n--- Main Menu ---")
        print("1. Administrator Functions")
        print("2. Reader Functions")
        print("3. Exit")

        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            password = input("Enter administrator password: ").strip()
            if password == "admin":
                print("Access granted. Welcome, Administrator!")
                admin_menu(library)
            else:
                print("Incorrect password. Access denied.")
        elif choice == 2:
            reader_menu(library)
        elif choice == 3:
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Create function admin_menu(library) for administrator.
def admin_menu(library):
    while True:
        print("\n--- Administrator Menu ---")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Back to main menu")

        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            add_book_interface(library)
        elif choice == 2:
            library.display_all_books()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

# Create function add_book_interface for administrator to add a new book to the library.
def add_book_interface(library):
    print("\n--- Add New Book ---")
    try:
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        isbn = input("Enter ISBN: ").strip()
        copies = int(input("Enter number of available copies: "))

        if title and author and isbn and copies >= 0:
            new_book = Book(title, author, isbn, copies)
            library.add_book(new_book)
        else:
            if not title:
                print("Title cannot be empty.")
            elif not author:
                print("Author name cannot be empty.")
            elif not isbn:
                print("ISBN cannot be empty.")
            elif copies < 0:
                print("Number of copies cannot be negative.")

    except ValueError:
        print("Invalid input for number of copies. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Create function reader_menu(library) for reader.
def reader_menu(library):
    while True:
        print("\n--- Reader Menu ---")
        print("1. Search for a book by title")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Display all books")
        print("5. Back to main menu")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            search_book_interface(library)
        elif choice == 2:
            borrow_book_interface(library)
        elif choice == 3:
            return_book_interface(library)
        elif choice == 4:
            library.display_all_books()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

# Create function search_book_interface(library) for reader to search a book by title.
def search_book_interface(library):
    print("\n--- Search Book ---")
    title = input("Enter the title of the book to search: ").strip()

    if not title:
        print("Title cannot be empty.")
        return
    book = library.find_book_by_title(title)
    if book:
        book.display_info()
    else:
        print(f"Book with title '{title}' not found in the library.")

# Create function borrow_book_interface(library) for reader to borrow a book.
def borrow_book_interface(library):
    print("\n--- Borrow Book ---")
    title = input("Enter the title of the book to borrow: ").strip()

    if not title:
        print("Title cannot be empty.")
        return
    book = library.find_book_by_title(title)
    if book:
        book.borrow_book()
        book.display_info()
    else:
        print(f"Book with title '{title}' not found in the library.")

# Create function borrow_book_interface(library) for reader to return a book.
def return_book_interface(library):
    print("\n--- Return Book ---")
    title = input("Enter the title of the book to return: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    book = library.find_book_by_title(title)
    if book:
        book.return_book()
        book.display_info()
    else:
        print(f"Book with title '{title}' not found in the library.")


if __name__ == "__main__":
    main()