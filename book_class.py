# book_class.py

class Book:
    """
    A class to represent a book with title, author, and publication year.
    Implements magic methods for object instantiation, deletion, and string representation.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize the Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor called when the object is about to be destroyed.
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"