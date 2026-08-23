"""
=========================================================
📚 LIBRARY MANAGEMENT SYSTEM (THE PROTOTYPE) 📚
=========================================================

Description:
    This is the humble beginning (Version 1.0) of what eventually 
    became a massive 2,700-line Library Management System. 
    It demonstrates the core OOP concepts (Classes, Instance Variables, 
    and Methods) that laid the foundation for the final project.

Created By: Lokendra Kushwaha
"""

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def show_info(self):
        print(f"The library has {self.no_of_books} books. The books are:")
        for book in self.books:
            print(f" ➔ {book}")

def main():
    print("=" * 50)
    print("       📚 BASIC LIBRARY SYSTEM PROTOTYPE 📚       ")
    print("=" * 50)
    
    l1 = Library()
    l1.add_book("Harry Potter - The Sorcerer's Stone")
    l1.add_book("Harry Potter - The Chamber of Secrets")
    l1.add_book("Harry Potter - The Prisoner of Azkaban")
    
    l1.show_info()
    
    print("-" * 50)
    print("Note: Books are not persisted after the program stops.")
    print("=" * 50)

if __name__ == "__main__":
    main()