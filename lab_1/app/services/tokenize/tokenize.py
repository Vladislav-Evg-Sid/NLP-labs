import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize, word_tokenize


def tokenize(texts: list[str]) -> list[list[str]]:
    result = []
    for text in texts:
        words = word_tokenize(text, language="russian")
        result.append(words)
    return result
