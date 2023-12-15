from datetime import datetime, timedelta

import pytest
from library import Library
import time

@pytest.fixture
def library():
    return Library()

def test_validate_quantity_negative(library):
    # Test validate_quantity for a negative quantity
    result = library.validate_quantity(-5)
    assert result == -1

def test_validate_quantity_zero(library):
    # Test validate_quantity for a quantity of zero
    result = library.validate_quantity(0)
    assert result == -1

def test_calculate_late_fee_zero_days(library):
    # Test calculate_late_fee for zero days overdue
    result = library.calculate_late_fee(0)
    assert result == 0

def test_calculate_late_fee_positive_days(library):
    # Test calculate_late_fee for positive days overdue
    result = library.calculate_late_fee(5)
    assert result == 5

def test_checkout_books_exceed_max_limit(library):
    # Test checkout_books for exceeding the maximum limit of books per checkout
    selections = [{'book_index': 1, 'quantity': 5}, {'book_index': 2, 'quantity': 6}]
    total_late_fee = library.checkout_books(selections)
    assert total_late_fee == -1

def test_return_books_overdue_with_late_fee(library):
    # Test return_books with overdue books and late fees
    checkout_selections = [{'book_index': 1, 'quantity': 1}]
    library.checkout_books(checkout_selections)

    # Move the due date to the past to simulate overdue books
    library.books[0].set_due_date(datetime.now() - timedelta(days=1))

    returned_books = [{'book_index': 1, 'quantity': 1}]
    total_late_fee = library.return_books(returned_books)
    assert total_late_fee > 0

def test_return_books_no_overdue(library):
    # Test return_books with no overdue books
    checkout_selections = [{'book_index': 1, 'quantity': 1}]
    library.checkout_books(checkout_selections)

    returned_books = [{'book_index': 1, 'quantity': 1}]
    total_late_fee = library.return_books(returned_books)
    assert total_late_fee == 0

def test_calculate_total_late_fees_with_overdue_books(library):
    # Test calculate_total_late_fees with overdue books
    checkout_selections = [{'book_index': 1, 'quantity': 1}]
    library.checkout_books(checkout_selections)

    # Move the due date to the past to simulate overdue books
    library.books[0].set_due_date(datetime.now() - timedelta(days=1))

    total_late_fee = library.calculate_total_late_fees()
    assert total_late_fee > 0