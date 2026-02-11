import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
from nltk.tokenize import sent_tokenize, word_tokenize


def tokenize(texts: list[str]) -> list[tuple[list[str], any]]: # TODO: Переписать сигнатуру
    result = []
    for text in texts:
        sentences = sent_tokenize(text, language='russian')
        words = word_tokenize(text, language='russian')
        result.append((sentences, words))
    return result
