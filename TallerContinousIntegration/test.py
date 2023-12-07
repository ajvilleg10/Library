import pytest
from library import Library
from main import select_books_for_checkout, process_book_returns

@pytest.fixture
def library():
    return Library()

def test_checkout_books(library):
    selections = [{'book_index': 1, 'quantity': 2}, {'book_index': 2, 'quantity': 1}]
    total_late_fee = library.checkout_books(selections)
    assert total_late_fee == 0  # Assuming no overdue books for this test

def test_process_book_returns(library):
    # Assume books are checked out first
    checkout_selections = [{'book_index': 1, 'quantity': 2}, {'book_index': 2, 'quantity': 1}]
    library.checkout_books(checkout_selections)

    returned_books = [{'book_index': 1, 'quantity': 1}]
    total_late_fee = library.return_books(returned_books)
    assert total_late_fee == 0  # Assuming no overdue books for this test

def test_calculate_total_late_fees(library):
    # Assuming no overdue books for this test
    total_late_fee = library.calculate_total_late_fees()
    assert total_late_fee == 0
