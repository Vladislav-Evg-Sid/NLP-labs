from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from pandas import Series
from typing import List
import numpy as np


def doc2vec(texts: Series, new_texts: List[str] = None):
    corpus_docs = [TaggedDocument(words=str(text).split(), tags=[i]) for i, text in enumerate(texts)]

    model = Doc2Vec(vector_size=100, min_count=1, epochs=40)
    model.build_vocab(corpus_docs)
    model.train(corpus_docs, total_examples=model.corpus_count, epochs=model.epochs)

    X = np.vstack([model.dv[i] for i in range(len(corpus_docs))])

    if new_texts is not None:
        X_new = np.vstack([model.infer_vector(str(text).split()) for text in new_texts])
        return X, X_new
    return X
