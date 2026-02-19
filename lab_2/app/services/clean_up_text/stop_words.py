from pandas import Series
import pandas as pd
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

english_stopwords = set(stopwords.words("english"))


def remove_stopwords(texts: Series) -> Series:
    def _remove(item):
        if isinstance(item, list):
            return [w for w in item if w.lower() not in english_stopwords]
        if isinstance(item, str):
            tokens = item.split()
            return " ".join([w for w in tokens if w.lower() not in english_stopwords])
        return item

    return texts.copy().apply(_remove)
