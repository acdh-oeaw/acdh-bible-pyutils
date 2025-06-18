import csv
import re
from pathlib import Path
from typing import Dict


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
            bible_books[book]["order"] = int(bible_books[book]["order"])
    return bible_books


BIBLE_BOOK_LOOKUP = get_bible_lookup_map()


def extract_book_name(reference: str) -> str:
    """
    Extract the book name from a biblical reference string.
    This function parses a biblical reference to extract just the book name portion,
    handling various formats including numbered books (e.g., "1 Kings", "2 Samuel")
    and books with multiple words. It also handles abbreviated book names that end
    with a period.
    Args:
        reference (str): A biblical reference string (e.g., "Genesis 1:1",
                        "1 Kings 2:3", "Matt. 5:7")
    Returns:
        str: The extracted book name with proper spacing and without trailing periods.
             If no match is found, returns the original reference string.
    """

    pattern = r"^(\d+\s*)?([A-Za-z]+\.?(?:\s+[A-Za-z]+)?)"
    match = re.match(pattern, reference)
    if match:
        book = "".join(part for part in match.groups() if part)
        book = " ".join(book.split())
        if book.endswith("."):
            return book[:-1]
        else:
            return book
    return reference


def get_book_from_bibl_ref(bibl_ref: str) -> Dict:
    """
    Retrieve book information from a biblical reference string.
    Args:
        bibl_ref (str): A biblical reference string containing a book name.
    Returns:
        dict: A dictionary containing book information with keys:
            - order (int): The order/position of the book (0 if not found)
            - title_eng (str): English title of the book
            - title_deu (str): German title of the book
            - title_lat (str): Latin title of the book
    Note:
        If the book is not found in BIBLE_BOOK_LOOKUP, returns a default
        dictionary with order=0 and the original bibl_ref as all titles.
    """

    sane_title = extract_book_name(bibl_ref)
    try:
        book = BIBLE_BOOK_LOOKUP[sane_title]
    except:
        book = {
            "order": 0,
            "title_eng": bibl_ref,
            "title_deu": bibl_ref,
            "title_lat": bibl_ref,
        }
    return book


def normalize_bible_refs(reference: str) -> dict:
    """
    Normalizes book info, chapter and verse numbers from biblical reference string.
    Returns a dictionary containing all book information plus chapter and verse numbers.

    Args:
        reference (str): Biblical reference (e.g., "Lk. 19,41" or "2 Kings 2:23-24")

    Returns:
        dict: Dictionary containing:
            - All keys from the book dictionary (order, title_eng, title_deu, title_lat)
            - chapter (int): Chapter number
            - verse_start (int): Starting verse number (0 if not present)
            - verse_end (int): Ending verse number (0 if not present)

    Examples:
        >>> extract_chapter_verses("Lk. 19,41")
        {
            'order': 49,
            'title_eng': 'Luke',
            'title_deu': 'Lukas',
            'title_lat': 'Lucas',
            'chapter': 19,
            'verse_start': 41,
            'verse_end': 0
        }
    """
    result = get_book_from_bibl_ref(reference)

    # Remove book name if present
    reference = re.sub(r"^(?:\d+\s+)?[A-Za-z]+\.?\s*(?:[A-ZaZ]+\s*)?", "", reference)

    # Pattern for different formats
    pattern = r"(\d+)(?:[\s,:]+(\d+))?(?:\s*[-–]\s*(\d+))?"

    match = re.search(pattern, reference)
    if match:
        result["chapter"] = int(match.group(1))
        result["verse_start"] = int(match.group(2)) if match.group(2) else 0
        result["verse_end"] = int(match.group(3)) if match.group(3) else 0
    else:
        result["chapter"] = 0
        result["verse_start"] = 0
        result["verse_end"] = 0

    return result
