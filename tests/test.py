import pytest
from acdh_bible_pyutils import extract_book_name


TEST_CASES = [
    ("Lk. 19,41", "Lk."),
    ("Mt. 27,52", "Mt."),
    ("2 Kings 2:23-24", "2 Kings"),
    ("4 Reg. 2,23", "4 Reg."),
    ("2 Sam. 6,16", "2 Sam."),
    ("2Sam 6,16", "2Sam"),
]


def test_extract_book_name():
    for reference, expected in TEST_CASES:
        result = extract_book_name(reference)
        assert (
            result == expected
        ), f"Expected '{expected}' but got '{result}' for reference '{reference}'"
