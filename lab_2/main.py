from app.services.loader.load_csv import parse_csv
from app.services.clean_up_text.clean_up_text import clean_up_text
from app.services.preprocessing.preprocess import preprocess
from app.services.processing_tfidf.processing import tfidf
from app.services.similarity.found import founding
from app.services.similarity.print_top import print_top


def processing(file_name: str):
    file_path = "lab_2/data/" + file_name
    data = parse_csv(file_path)
    data["overview_preproc"] = clean_up_text(data["overview"])
    data["overview_preproc"] = preprocess(data["overview_preproc"])
    return data


def main():
    names = ["tmdb_5000_movies.csv", "new_texts.csv"]
    data_1 = processing(names[0])
    data_2 = processing(names[1])

    X_old, X_new = tfidf(data_1["overview_preproc"], data_2["overview_preproc"])
    tops = founding(X_old, X_new)
    print_top(tops, data_1, data_2)


if __name__ == "__main__":
    main()
