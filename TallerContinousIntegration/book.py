# File: book.py
from datetime import datetime, timedelta

class Book:
    """
    Represents a book in the library.

    Attributes:
    - title (str): The title of the book.
    - author (str): The author of the book.
    - quantity (int): The quantity of available copies.
    - due_date (datetime): The due date for the book if checked out.
    - availability (bool): True if available, False if checked out.
    """

    def __init__(self, title, author, quantity):
        """Initializes a new instance of the Book class."""
        self.title = title
        self.author = author
        self.quantity = quantity
        self.due_date = None
        self.availability = True

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_due_date(self):
        return self.due_date

    def set_due_date(self, due_date):
        self.due_date = due_date

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability
