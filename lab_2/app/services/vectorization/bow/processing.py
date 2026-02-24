from sklearn.feature_extraction.text import CountVectorizer
from pandas import Series

vectorizer = CountVectorizer()


def bow(texts: Series, new_texts: list[str] | None = None):
    corpus = list(texts)
    X = vectorizer.fit_transform(corpus)
    if new_texts is not None:
        X_new = vectorizer.transform(new_texts)
        return X, X_new
    return X
