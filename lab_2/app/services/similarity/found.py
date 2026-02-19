from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def top_k_indices(sim_row, k: int) -> list[tuple[int, float]]:
    indices = np.argsort(sim_row)[::-1][:k]
    return [(int(idx), float(sim_row[idx])) for idx in indices]


def founding(X, new_X):
    similarity_matrix = cosine_similarity(new_X, X)
    top_list = []
    for i in range(len(similarity_matrix)):
        top_5 = top_k_indices(similarity_matrix[i], 5)
        top_list.append(top_5)
    return top_list
