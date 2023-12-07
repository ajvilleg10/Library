# File: main.py
from library import Library

def get_positive_integer_input(prompt):
    """Get positive integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Please enter a positive integer.")
            return value
        except ValueError as e:
            print(f"Error: {e}")

def display_menu():
    """Display the menu of options."""
    print("\nMenu:")
    print("1. Display Book Catalog")
    print("2. Checkout Books")
    print("3. Process Book Returns")
    print("4. Calculate Total Late Fees")
    print("5. Exit")
    return get_positive_integer_input("Enter your choice (1-5): ")

def display_book_catalog(library):
    """Display the catalog of available books."""
    library.display_catalog()

def select_books_for_checkout(library):
    """Select books for checkout and specify the quantity."""
    library.display_catalog()
    selections = []

    while True:
        book_index = get_positive_integer_input("Enter the book index to checkout (-1 to finish): ")

        if book_index == -1:
            break

        while not (1 <= book_index <= len(library.books)):
            print(f"Error: Invalid book index. Please enter a valid book index between 1 and {len(library.books)}.")
            book_index = get_positive_integer_input("Enter the book index to checkout (-1 to finish): ")

        quantity = library.validate_quantity(get_positive_integer_input("Enter the quantity to checkout: "))
        if quantity == -1:
            continue

        selections.append({'book_index': book_index, 'quantity': quantity})

        # Ask if the user wants to continue
        user_input = input("Do you want to continue adding books to the checkout? (y/n): ").lower()
        if user_input != 'y':
            break

    return selections

def process_book_returns(library):
    """Process book returns by entering the book details."""
    returned_books = []

    while True:
        book_index = get_positive_integer_input("Enter the book index to return (-1 to finish): ")

        if book_index == -1:
            break

        while not (1 <= book_index <= len(library.books)):
            print(f"Error: Invalid book index. Please enter a valid book index between 1 and {len(library.books)}.")
            book_index = get_positive_integer_input("Enter the book index to return (-1 to finish): ")

        quantity = library.validate_quantity(get_positive_integer_input("Enter the quantity to return: "))
        if quantity == -1:
            continue

        returned_books.append({'book_index': book_index, 'quantity': quantity})

        # Ask if the user wants to continue
        user_input = input("Do you want to continue adding books to the return? (y/n): ").lower()
        if user_input != 'y':
            break

    total_late_fee = library.return_books(returned_books)

    if total_late_fee > 0:
        print(f"Total late fees for returned books: ${total_late_fee}")

def calculate_total_late_fees(library):
    """Calculate and display the total late fees accrued for all overdue books."""
    total_late_fee = library.calculate_total_late_fees()
    print(f"Total late fees for all overdue books: ${total_late_fee}")

def main():
    library = Library()

    while True:
        choice = display_menu()

        if choice == 1:
            display_book_catalog(library)
        elif choice == 2:
            selections = select_books_for_checkout(library)
            if selections:
                library.checkout_books(selections)
        elif choice == 3:
            process_book_returns(library)
        elif choice == 4:
            calculate_total_late_fees(library)
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
