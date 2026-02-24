from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import Series

vectorizer = TfidfVectorizer()


def tfidf(texts: Series, new_texts: list[str] = None):
    corpus = list(texts)
    X = vectorizer.fit_transform(corpus)
    if new_texts is not None:
        X1 = vectorizer.transform(new_texts)
        return X, X1
    return X
