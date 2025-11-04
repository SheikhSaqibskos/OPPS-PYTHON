from abc import ABC, abstractmethod

# ------------------------------
# 1️⃣ Abstraction
# ------------------------------
class LibraryItem(ABC):
    def __init__(self, title, author):
        self._title = title         # Protected attribute
        self._author = author

    @abstractmethod
    def display_info(self):
        pass


# ------------------------------
# 2️⃣ Inheritance + 3️⃣ Polymorphism
# ------------------------------
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):   # Polymorphism: same function, different behavior
        print(f"Book: {self._title} by {self._author}, Pages: {self.pages}")


class Magazine(LibraryItem):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine: {self._title} by {self._author}, Issue: {self.issue_number}")


# ------------------------------
# 4️⃣ Encapsulation
# ------------------------------
class Library:
    def __init__(self):
        self.__items = []   # Private attribute

    def add_item(self, item):
        self.__items.append(item)
        print(f"Added: {item._title}")

    def show_items(self):
        print("\n📚 Library Collection:")
        for item in self.__items:
            item.display_info()   # Polymorphism in action


# ------------------------------
# Using the classes
# ------------------------------
book1 = Book("Python Basics", "John Smith", 300)
book2 = Book("OOP Concepts", "Jane Doe", 220)
mag1 = Magazine("Tech Today", "TechWorld", 45)

library = Library()
library.add_item(book1)
library.add_item(book2)
library.add_item(mag1)

library.show_items()
