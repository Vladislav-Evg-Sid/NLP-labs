from sklearn.manifold import TSNE
import numpy as np
from typing import Tuple, Union


def _to_dense(mat):
    if hasattr(mat, "toarray"):
        return mat.toarray()
    return np.asarray(mat)


def tsne(Xs: Union[Tuple, object], random_state: int = 42, **kwargs):
    # Собираем список матриц
    if isinstance(Xs, (list, tuple)):
        X_old, X_new = Xs[0], Xs[1]
        X_old_d = _to_dense(X_old)
        X_new_d = _to_dense(X_new)
        stacked = np.vstack([X_old_d, X_new_d])
        tsne_model = TSNE(n_components=2, random_state=random_state, **kwargs)
        reduced = tsne_model.fit_transform(stacked)
        n_old = X_old_d.shape[0]
        return reduced[:n_old], reduced[n_old:]

    # одиночный вход
    X = _to_dense(Xs)
    tsne_model = TSNE(n_components=2, random_state=random_state, **kwargs)
    reduced = tsne_model.fit_transform(X)
    return reduced
