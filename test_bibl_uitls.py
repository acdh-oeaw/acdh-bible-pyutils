from acdh_bible_pyutils import extract_book_name, get_book_from_bibl_ref


TEST_CASES = [
    ("Lk. 19,41", "Lk"),
    ("Mt. 27,52", "Mt"),
    ("2 Kings 2:23-24", "2 Kings"),
    ("4 Reg. 2,23", "4 Reg"),
    ("2 Sam. 6,16", "2 Sam"),
    ("88Fran 6,16", "88Fran"),
    ("88 Fran 6,16", "88 Fran"),
]

BOOK_TESTS = [
    (
        "Lk. 19,41",
        {"order": 51, "title_eng": "Luke", "title_deu": "Lukas", "title_lat": "Lucas"},
    ),
    (
        "2 Kings 2:23-24",
        {
            "order": 12,
            "title_eng": "2 Kings",
            "title_deu": "2. Könige",
            "title_lat": "2 Regnum",
        },
    ),
    (
        "88 Fran 6,16",
        {
            "order": 0,
            "title_eng": "88 Fran",
            "title_deu": "88 Fran",
            "title_lat": "88 Fran",
        },
    ),
]


def test__01__extract_book_name():
    for reference, expected in TEST_CASES:
        result = extract_book_name(reference)
        assert (
            result == expected
        ), f"Expected '{expected}' but got '{result}' for reference '{reference}'"


def test___02__get_book_from_bibl_ref():
    for reference, expected in BOOK_TESTS:
        book = get_book_from_bibl_ref(reference)
        assert book["order"] == expected["order"]
