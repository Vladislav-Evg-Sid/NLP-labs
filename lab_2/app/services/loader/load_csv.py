import pandas as pd


def parse_csv(
    file_path: str, text_column=["original_title", "overview"], encoding: str = "utf-8"
) -> pd.DataFrame:
    try:
        separators = [",", ";", "\t", "|"]

        for sep in separators:
            try:
                df = pd.read_csv(file_path, sep=sep, encoding=encoding)
                texts = df[text_column].dropna()
                return texts
            except:
                continue

        print(f"Не найдена колонка '{text_column}' в файле {file_path}")
        return []

    except Exception as e:
        print(f"Ошибка при парсинге CSV файла {file_path}: {e}")
        return []
