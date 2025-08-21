wanted_book = input()

checked_book_count = 0

while True:
    current_book = input()

    if current_book == "No More Books":
        print(f"The book you search is not here!\nYou checked {checked_book_count} books.")
        break

    if wanted_book == current_book:
        print(f"You checked {checked_book_count} books and found it.")
        break

    checked_book_count += 1