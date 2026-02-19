from pandas import Series

from nltk.stem import WordNetLemmatizer
import nltk

nltk.download("wordnet")

lemmat = WordNetLemmatizer()


def get_wordnet_pos(tag: str) -> str:
    handler = {"J": "a", "V": "v", "N": "n", "R": "r"}
    for key, value in handler.items():
        if tag.startswith(key):
            return value
    return "n"


def lemmatizer(texts: Series):
    texts = texts.copy()
    for i in range(len(texts)):
        lemmas = []
        for word, tag in texts.iloc[i]:
            lemmas.append(lemmat.lemmatize(word, get_wordnet_pos(tag)))
        texts.iloc[i] = lemmas
    return texts
