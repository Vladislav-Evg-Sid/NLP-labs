from app.services.loader.load_csv import parse_csv
from app.services.clean_up_text.clean_up_text import clean_up_text
from app.services.preprocessing.preprocess import preprocess
from app.services.vectorization.tfidf.processing import tfidf
from app.services.vectorization.glove.processing import glove
from app.services.vectorization.bow.processing import bow
from app.services.vectorization.doc2vec.processing import doc2vec
from app.services.similarity.found import founding
from app.services.similarity.print_top import print_top
from app.services.dimensional_reduction.tsne.processing import tsne
from app.services.dimensional_reduction.umap.processing import umap_reduce

from pandas import DataFrame


def processing(file_name: str) -> DataFrame:
    file_path = "lab_2/data/" + file_name
    data = parse_csv(file_path, text_column=["original_title", "overview", "genres"])
    data["overview_preproc"] = clean_up_text(data["overview"])
    data["overview_preproc"] = preprocess(data["overview_preproc"])
    return data


def main_similarity():
    names = ["tmdb_5000_movies.csv", "new_texts.csv"]
    data_main = processing(names[0])
    data_new5 = processing(names[1])

    print(">>> TF-IDF")
    X_old, X_new = tfidf(data_main["overview_preproc"], data_new5["overview_preproc"])
    tops = founding(X_old, X_new)
    print_top(tops, data_main, data_new5)

    print(">>> GloVe")
    X_old = glove(data_main["overview_preproc"])
    X_new = glove(data_new5["overview_preproc"])
    tops = founding(X_old, X_new)
    print_top(tops, data_main, data_new5)

    print(">>> Bag of Words")
    X_old, X_new = bow(data_main["overview_preproc"], data_new5["overview_preproc"])
    tops = founding(X_old, X_new)
    print_top(tops, data_main, data_new5)

    print(">>> Doc2vec")
    X_old, X_new = doc2vec(data_main["overview_preproc"], data_new5["overview_preproc"])
    tops = founding(X_old, X_new)
    print_top(tops, data_main, data_new5)


def main_graphics():
    data = processing("tmdb_5000_movies.csv")
    X = doc2vec(data["overview_preproc"])
    print('*'*100)
    print(tsne(X))
    print('*'*100)
    print(umap_reduce(X))
    print('*'*100)


if __name__ == "__main__":
    main_graphics()
