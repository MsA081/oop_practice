from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    @abstractmethod
    def check_out(self, book_name):
        pass

    @abstractmethod
    def check_in(self, book_name):
        pass


class Library(Book):
    def __init__(self, name, title, author):
        self.name = name
        super().__init__(title, author)
        self.books = []

    def check_out(self, book_name):
        for book in self.books:
            if book["book_name"] == book_name:
                book["available"] = False
                return f"Book {book_name} checked out successfully."

    def check_in(self, book_name):
        for book in self.books:
            if book["book_name"] == book_name:
                book["available"] = True
                return f"Book {book_name} checked in successfully."

    def add_book(self, book_name, title, author):
        for book in self.books:
            if book["book_name"] == book_name:
                return f"Book {book_name} already exists."
        self.books.append({"book_name": book_name,
                           "title": title,
                           "author": author,
                           "available": True})
        return f"Book {book_name} added successfully."

    def remove_book(self, book_name):
        for book in self.books:
            if book["book_name"] == book_name:
                self.books.remove(book)
                return f"Book {book_name} removed successfully."
        return f"Book {book_name} not found."

    def search_book(self, title_search):
        print(f"searched by: {title_search}")
        for book in self.books:
            if book["title"] == title_search:
                print(book)
        return f"Book with title {title_search} not found."

    def display_books(self):
        print(f"Book details: ")
        for book in self.books:
            print(f"Book Name: {book['book_name']}\t"
                  f"Title: {book['title']}\t"
                  f"Author: {book['author']}\t"
                  f"Available: {book['available']}")


# Test the implementation
library = Library("Library1", "back-end", "Mohammad")

# Display library info
library.display_books()

# Check out and check in a book
print(library.add_book("python3", "back-end", "Mohammad"))
library.display_books()

print(library.check_out("python3"))
library.display_books()

print(library.check_in("python3"))
library.display_books()

# Add more books
print(library.add_book("django", "back-end", "MohammadSina"))
library.display_books()

print(library.add_book("react", "front-end", "MohammadSina"))
library.display_books()

# Search for a book
library.search_book("back-end")

# Remove a book
print(library.remove_book("python3"))
library.display_books()
