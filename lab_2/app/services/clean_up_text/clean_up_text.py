from pandas import Series
import pandas as pd


def to_lower(texts: Series) -> Series:
    return texts.str.lower()


def delete_number(texts: Series) -> Series:
    return texts.str.replace(r"\d", "", regex=True)


def delete_punct(texts: Series) -> Series:
    texts = texts.str.replace(" - ", " ", regex=False)
    return texts.str.replace(r"[,;:'\"()\.\!\?]", "", regex=True)


def delete_spaces(texts: Series) -> Series:
    return texts.str.replace(r"\s+", " ", regex=True).str.strip()


def clean_up_text(input_texts: Series) -> Series:
    texts = input_texts.copy()
    texts = to_lower(texts)
    texts = delete_number(texts)
    texts = delete_punct(texts)
    texts = delete_spaces(texts)
    return texts
