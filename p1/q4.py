from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        return f"Title: {self.title}\tAuthor: {self.author}\tAvailable: {self.is_available}\n"

    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def check_in(self):
        pass


class Library(Book):

    def __init__(self, name, books, title, author):
        self.name = name
        self.books = books
        super().__init__(title, author)

    def check_out(self):
        self.is_available = False

    def check_in(self):
        self.is_available = True

    def add_book(self, book_name):
        if book_name not in self.books:
            self.books.append(book_name)
            return self.books

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            return self.books

    def search_book(self, title_search):
        for book in self.books:
            if title_search == self.title:
                return book

    def display_books(self):
        for book in self.books:
            print(f"book_name : {book}\t"
                  f"title: {self.title}\t"
                  f"author: {self.author}\t"
                  f"available: {self.is_available}\n")


book1 = Book("python3", "mohammad")
print(book1.display_info())
book1.check_out()
print(book1.display_info())
book1.check_in()
print(book1.display_info())

library1 = Library("library1", ("b1", "b2", "b3", "b4"))
library1.display_books()
library1.check_out()
library1.display_books()
library1.check_in()
library1.display_books()
print(library1.add_book(book1))
library1.display_books()
print(library1.remove_book("b2"))
library1.display_books()
print(library1.search_book("python3"))
library1.display_books()
