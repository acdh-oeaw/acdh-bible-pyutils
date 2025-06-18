from acdh_bible_pyutils import (
    extract_book_name,
    get_book_from_bibl_ref,
    normalize_bible_refs,
)

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
        assert result == expected, f"Expected '{expected}' but got '{result}' for reference '{reference}'"


def test__02__get_book_from_bibl_ref():
    for reference, expected in BOOK_TESTS:
        book = get_book_from_bibl_ref(reference)
        assert book["order"] == expected["order"]


def test__03__normalize_bible_refs():
    bible_refs = [
        "Lk. 19,41-50",
        "Mt. 27,52",
        "2 Kings 2:23-24",
        "4 Reg. 2,23",
        "2 Sam. 6,16",
        "88Sam 6,16",
    ]
    results = [
        {
            "order": 51,
            "title_eng": "Luke",
            "title_deu": "Lukas",
            "title_lat": "Lucas",
            "chapter": 19,
            "verse_start": 41,
            "verse_end": 50,
        },
        {
            "order": 49,
            "title_eng": "Matthew",
            "title_deu": "Matthäus",
            "title_lat": "Matthaeus",
            "chapter": 27,
            "verse_start": 52,
            "verse_end": 0,
        },
        {
            "order": 12,
            "title_eng": "2 Kings",
            "title_deu": "2. Könige",
            "title_lat": "2 Regum",
            "chapter": 2,
            "verse_start": 23,
            "verse_end": 24,
        },
        {
            "order": 14,
            "title_eng": "4 Kings",
            "title_deu": "4. Könige",
            "title_lat": "4 Regum",
            "chapter": 2,
            "verse_start": 23,
            "verse_end": 0,
        },
        {
            "order": 10,
            "title_eng": "2 Samuel",
            "title_deu": "2. Samuel",
            "title_lat": "2 Samuel",
            "chapter": 6,
            "verse_start": 16,
            "verse_end": 0,
        },
        {
            "order": 0,
            "title_eng": "88Sam 6,16",
            "title_deu": "88Sam 6,16",
            "title_lat": "88Sam 6,16",
            "chapter": 88,
            "verse_start": 0,
            "verse_end": 0,
        },
    ]

    for i, x in enumerate(bible_refs):
        normalized_ref = normalize_bible_refs(x)
        assert normalized_ref == results[i]
