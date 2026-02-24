from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import Series

vectorizer = TfidfVectorizer()


def tfidf(texts: Series, new_texts: list[str]):
    corpus = list(texts)
    X = vectorizer.fit_transform(corpus)
    X1 = vectorizer.transform(new_texts)
    return X, X1
