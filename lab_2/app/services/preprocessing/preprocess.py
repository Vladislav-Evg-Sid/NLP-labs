from app.services.preprocessing.tokenize import tokenizer
from app.services.preprocessing.lemmatize import lemmatizer
from app.services.clean_up_text.clean_up_text import clean_up_text
from app.services.clean_up_text.stop_words import remove_stopwords

import pandas as pd


def preprocess(texts: pd.Series) -> pd.Series:
    texts = texts.copy()
    texts = clean_up_text(texts)
    tagged_tokens = tokenizer(texts)
    lemmas = lemmatizer(tagged_tokens)
    lemmas = remove_stopwords(lemmas)
    lemmatized_texts = lemmas.apply(lambda x: " ".join(x) if isinstance(x, list) else x)
    return lemmatized_texts
