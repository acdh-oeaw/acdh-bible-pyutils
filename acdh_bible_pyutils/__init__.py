import csv
import re
from pathlib import Path


def get_bible_lookup_map() -> dict:
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


BIBLE_BOOK_LOOKUP = get_bible_lookup_map()


def extract_book_name(reference: str) -> str:
    """
    Extract book name from biblical reference string.

    Args:
        reference (str): Full biblical reference (e.g., "Lk. 19,41" or "2 Kings 2:23-24")

    Returns:
        str: Extracted book name

    Examples:
        >>> extract_book_name("Lk. 19,41")
        'Lk.'
        >>> extract_book_name("2 Kings 2:23-24")
        '2 Kings'
    """
    pattern = r"^([1-4]\s*)?([A-Za-z]+\.?(?:\s+[A-Za-z]+)?)"
    match = re.match(pattern, reference)
    if match:
        book = "".join(part for part in match.groups() if part)
        # Clean up any extra spaces
        return " ".join(book.split())
    return ""
