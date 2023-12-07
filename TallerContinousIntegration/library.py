# File: library.py
from datetime import datetime, timedelta
from book import Book

class Library:
    MAX_BOOKS_PER_CHECKOUT = 10

    def __init__(self):
        """Initializes a new instance of the Library class."""
        self.books = [
            Book("Book1", "Author1", 5),
            Book("Book2", "Author2", 3),
            # Add more books as needed
        ]

    def display_catalog(self):
        """Display the catalog of available books."""
        print("\nLibrary Book Catalog:")
        for i, book in enumerate(self.books, 1):
            availability = "Available" if book.get_availability() else "Not Available"
            print(f"{i}. Title: {book.get_title()}, Author: {book.get_author()}, Quantity: {book.get_quantity()}, Availability: {availability}")

    def validate_quantity(self, quantity):
        """Validate that the quantity entered is a positive integer greater than zero."""
        if quantity <= 0:
            print("Error: Quantity must be a positive integer greater than zero.")
            return -1
        return quantity

    def calculate_due_date(self):
        """Calculate the due date based on the current date and the standard loan period."""
        return datetime.now() + timedelta(days=14)

    def calculate_late_fee(self, days_overdue):
        """Calculate the late fee based on the number of days overdue."""
        return days_overdue * 1  # $1 per day late fee

    def checkout_books(self, selections):
        """Checkout selected books and calculate late fees."""
        total_late_fee = 0
        selected_books_info = []

        total_selected_books = sum(selection['quantity'] for selection in selections)
        if total_selected_books > self.MAX_BOOKS_PER_CHECKOUT:
            print(f"Error: Maximum {self.MAX_BOOKS_PER_CHECKOUT} books allowed per checkout. Adjust your selection.")
            return -1

        for selection in selections:
            book_index = selection['book_index']
            quantity = selection['quantity']

            book = self.books[book_index - 1]
            book_info = {
                'title': book.get_title(),
                'author': book.get_author(),
                'quantity': quantity,
                'due_date': self.calculate_due_date(),
            }
            selected_books_info.append(book_info)

            if book.get_due_date() and datetime.now() > book.get_due_date():
                days_overdue = (datetime.now() - book.get_due_date()).days
                late_fee = self.calculate_late_fee(days_overdue)
                total_late_fee += late_fee

            # Actualizar la cantidad al hacer el checkout
            book.set_quantity(book.get_quantity() - quantity)

        print("\nSelected Books for Checkout:")
        for info in selected_books_info:
            print(f"Title: {info['title']}, Author: {info['author']}, Quantity: {info['quantity']}, Due Date: {info['due_date']}")

        confirm_input = input("Do you want to confirm the checkout? (y/n): ").lower()
        if confirm_input != 'y':
            print("Checkout canceled. Make changes to your selections.")
            for info in selected_books_info:
                book = self.books[selection['book_index'] - 1]
                book.set_quantity(book.get_quantity() + info['quantity'])
            return -1

        for info in selected_books_info:
            book = self.books[selection['book_index'] - 1]
            book.set_due_date(info['due_date'])

        print("Checkout successful.")
        print("Due Dates:")
        for info in selected_books_info:
            print(f"{info['title']}: {info['due_date']}")

        if total_late_fee > 0:
            print(f"Total late fees: ${total_late_fee}")

        return total_late_fee

    def return_books(self, returned_books):
        """Process book returns and calculate additional late fees."""
        total_late_fee = 0
        for returned_book in returned_books:
            book_index = returned_book['book_index']
            quantity = returned_book['quantity']

            book = self.books[book_index - 1]

            if book.get_due_date() and datetime.now() > book.get_due_date():
                days_overdue = (datetime.now() - book.get_due_date()).days
                late_fee = self.calculate_late_fee(days_overdue)
                total_late_fee += late_fee

            # Actualizar la cantidad al procesar la devolución
            book.set_quantity(book.get_quantity() + quantity)

        print("Return process successful.")
        print("Updated Status of Returned Books:")
        for returned_book in returned_books:
            book = self.books[returned_book['book_index'] - 1]
            availability = "Available" if book.get_availability() else "Not Available"
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Quantity Returned: {returned_book['quantity']}, Updated Quantity: {book.get_quantity()}, Availability: {availability}")

        if total_late_fee > 0:
            print(f"Total late fees for returned books: ${total_late_fee}")

        return total_late_fee

    def calculate_total_late_fees(self):
        """Calculate the total late fees accrued for all overdue books."""
        total_late_fee = 0
        for book in self.books:
            if book.get_due_date() and datetime.now() > book.get_due_date():
                days_overdue = (datetime.now() - book.get_due_date()).days
                late_fee = self.calculate_late_fee(days_overdue)
                total_late_fee += late_fee

        return total_late_fee
