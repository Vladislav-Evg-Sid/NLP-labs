import gensim.downloader as api
import numpy as np

model = api.load("glove-wiki-gigaword-300")


def text_to_vector(text, model, vector_size=300):
    words = text.split()  # текст уже предобработан и лемматизирован
    word_vectors = []

    for word in words:
        try:
            # Пытаемся получить вектор слова
            vec = model[word]
            word_vectors.append(vec)
        except KeyError:
            # Слово отсутствует в словаре модели — пропускаем
            continue

    if len(word_vectors) == 0:
        # Если ни одного слова не нашлось, возвращаем нулевой вектор
        return np.zeros(vector_size)

    # Усредняем все векторы слов
    return np.mean(word_vectors, axis=0)


def glove(texts):
    result = []
    for i in range(len(texts)):
        result.append(text_to_vector(texts.iloc[i], model))
    return np.array(result)
