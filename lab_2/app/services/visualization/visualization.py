import matplotlib.pyplot as plt
import numpy as np
from pandas import Series
from typing import Tuple, Optional


def scatter_by_genres(X: object, genres: Series, title: Optional[str] = None, figsize: Tuple[int, int] = (10, 8), s: int = 30, alpha: float = 0.7):
    X_arr = np.asarray(X)
    if X_arr.ndim != 2 or X_arr.shape[1] != 2:
        raise ValueError('Ожидается массив формы (n_samples, 2)')

    genres = Series(genres).fillna('Unknown').astype(str)
    primary = genres.apply(lambda g: g.split('|')[0].strip() if g else 'Unknown')
    unique_genres = sorted(primary.unique())

    cmap = plt.get_cmap('tab20')
    color_map = {g: cmap(i % cmap.N) for i, g in enumerate(unique_genres)}

    fig, ax = plt.subplots(figsize=figsize)

    for g in unique_genres:
        mask = primary == g
        pts = X_arr[mask.values]
        if pts.shape[0] == 0:
            continue
        ax.scatter(pts[:, 0], pts[:, 1], label=g, c=[color_map[g]], s=s, alpha=alpha, edgecolors='w', linewidths=0.3)

    ax.set_xlabel('dim 1')
    ax.set_ylabel('dim 2')
    if title:
        ax.set_title(title)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
    plt.tight_layout()
    try:
        plt.show(block=False)
        plt.pause(0.1)
    except Exception:
        pass

    return fig, ax
