import numpy as np
from typing import Tuple, Union
from umap import UMAP


def _to_dense(mat):
    if hasattr(mat, "toarray"):
        return mat.toarray()
    return np.asarray(mat)


def umap_reduce(Xs: Union[Tuple, object], n_neighbors: int = 15, min_dist: float = 0.1, random_state: int = 42, **kwargs):
    if isinstance(Xs, (list, tuple)):
        X_old, X_new = Xs[0], Xs[1]
        X_old_d = _to_dense(X_old)
        X_new_d = _to_dense(X_new)
        stacked = np.vstack([X_old_d, X_new_d])
        umap_model = UMAP(n_components=2, n_neighbors=n_neighbors, min_dist=min_dist, random_state=random_state, **kwargs)
        reduced = umap_model.fit_transform(stacked)
        n_old = X_old_d.shape[0]
        return reduced[:n_old], reduced[n_old:]

    X = _to_dense(Xs)
    umap_model = UMAP(n_components=2, n_neighbors=n_neighbors, min_dist=min_dist, random_state=random_state, **kwargs)
    reduced = umap_model.fit_transform(X)
    return reduced
