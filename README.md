# acdh-bible-pyutils

Utility functions for dealing with biblicial references


## install

```shell
pip install acdh-bible-pyutils
```
or
```shell
uv add acdh-bible-pyutils
```

## use

### get bible book from biblical reference

```python
from acdh_bible_pyutils import get_book_from_bibl_ref, BIBLE_BOOK_LOOKUP


book = get_book_from_bibl_ref("Lk. 19,41")
print(book)
>>> {"order": 51, "title_eng": "Luke", "title_deu": "Lukas", "title_lat": "Lucas"}

bible_refs = [
    "Lk. 19,41",
    "Mt. 27,52",
    "2 Kings 2:23-24",
    "4 Reg. 2,23",
    "2 Sam. 6,16",
    "88Sam 6,16",
]
for x in bible_refs:
    book = get_book_from_bibl_ref(x)
    print(f"{x} resolves to: **{book["title_lat"]} / {book["title_deu"]}**, order-nr: {book["order"]}")

>>> Lk. 19,41 resolves to: **Lucas / Lukas**, order-nr: 51
>>> Mt. 27,52 resolves to: **Matthaeus / Matthäus**, order-nr: 49
>>> 2 Kings 2:23-24 resolves to: **2 Regum / 2. Könige**, order-nr: 12
>>> 4 Reg. 2,23 resolves to: **4 Regum / 4. Könige**, order-nr: 14
>>> 2 Sam. 6,16 resolves to: **2 Samuel / 2. Samuel**, order-nr: 10
>>> 88Sam 6,16 resolves to: **88Sam 6,16 / 88Sam 6,16**, order-nr: 0


BIBLE_BOOK_LOOKUP["Lk"]
>>> {"order": 51, "title_eng": "Luke", "title_deu": "Lukas", "title_lat": "Lucas"}
```

### normalize biblical references
```python
from acdh_bible_pyutils import normalize_bible_refs
bible_refs = [
    "Lk. 19,41-50",
    "Mt. 27,52",
    "2 Kings 2:23-24",
    "4 Reg. 2,23",
    "2 Sam. 6,16",
    "88Sam 6,16",
]
for x in bible_refs:
    print(normalize_bible_refs(x))
>>> {"order": 51, "title_eng": "Luke", "title_deu": "Lukas", "title_lat": "Lucas", "chapter": 19, "verse_start": 41, "verse_end": 50}
>>> {"order": 49, "title_eng": "Matthew", "title_deu": "Matthäus", "title_lat": "Matthaeus", "chapter": 27, "verse_start": 52, "verse_end": 0}
>>> {"order": 12, "title_eng": "2 Kings", "title_deu": "2. Könige", "title_lat": "2 Regum", "chapter": 2, "verse_start": 23, "verse_end": 24}
>>> {"order": 14, "title_eng": "4 Kings", "title_deu": "4. Könige", "title_lat": "4 Regum", "chapter": 2, "verse_start": 23, "verse_end": 0}
>>> {"order": 10, "title_eng": "2 Samuel", "title_deu": "2. Samuel", "title_lat": "2 Samuel", "chapter": 6, "verse_start": 16, "verse_end": 0}
>>> {"order": 0, "title_eng": "88Sam 6,16", "title_deu": "88Sam 6,16", "title_lat": "88Sam 6,16", "chapter": 88, "verse_start": 0, "verse_end": 0}

## build

```shell
uv build
```


## cheat sheet

### sort imports
```shell
ruff check --select I --fix
```

### format files
```shell
ruff format
```

### run tests

```shell
uv run pytest
```