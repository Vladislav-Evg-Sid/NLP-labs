from app.services.loader.load_csv import parse_csv


def main():
    file_path = "lab_2/data/tmdb_5000_movies.csv"
    data = parse_csv(file_path)
    print(data)


if __name__ == "__main__":
    main()
