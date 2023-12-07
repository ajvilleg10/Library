import unittest
from library import Library
from main import select_books_for_checkout, process_book_returns

class TestLibraryMethods(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_checkout_books(self):
        selections = [{'book_index': 1, 'quantity': 2}, {'book_index': 2, 'quantity': 1}]
        total_late_fee = self.library.checkout_books(selections)
        self.assertEqual(total_late_fee, 0)  # Assuming no overdue books for this test

    def test_process_book_returns(self):
        # Assume books are checked out first
        checkout_selections = [{'book_index': 1, 'quantity': 2}, {'book_index': 2, 'quantity': 1}]
        self.library.checkout_books(checkout_selections)

        returned_books = [{'book_index': 1, 'quantity': 1}]
        total_late_fee = self.library.return_books(returned_books)
        self.assertEqual(total_late_fee, 0)  # Assuming no overdue books for this test

    def test_calculate_total_late_fees(self):
        # Assuming no overdue books for this test
        total_late_fee = self.library.calculate_total_late_fees()
        self.assertEqual(total_late_fee, 0)

#Ejecución del main
if __name__ == '__main__':
    unittest.main()
