import csv
from pathlib import Path


def get_bible_books() -> dict:
    """
    Load and return Bible book information from a CSV file.
    Reads Bible book data from 'bible_books.csv' located in the same directory
    as this module. The CSV file is expected to have a 'book' column that serves
    as the key, with remaining columns becoming the associated metadata for each book.
    Returns:
        dict: A dictionary where keys are book names (from the 'book' column)
              and values are dictionaries containing the remaining row data
              for each book.
    Raises:
        FileNotFoundError: If the bible_books.csv file is not found.
        csv.Error: If there's an error reading the CSV file.
        UnicodeDecodeError: If there's an encoding issue with the file.
    """

    bible_books = {}
    csv_path = Path(__file__).parent / "bible_books.csv"

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = row.pop("book")
            bible_books[book] = row
    return bible_books


BIBLE_BOOKS = get_bible_books


