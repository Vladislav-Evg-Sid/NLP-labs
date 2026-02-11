import pandas as pd


def parse_csv(
    file_path: str, text_column: str = "text", encoding: str = "utf-8"
) -> list[str]:
    try:
        separators = [",", ";", "\t", "|"]

        for sep in separators:
            try:
                df = pd.read_csv(file_path, sep=sep, encoding=encoding)
                if text_column in df.columns:
                    texts = df[text_column].dropna().astype(str).tolist()
                    texts = [text.strip() for text in texts if text.strip()]
                    return texts
            except:
                continue

        print(f"Не найдена колонка '{text_column}' в файле {file_path}")
        return []

    except Exception as e:
        print(f"Ошибка при парсинге CSV файла {file_path}: {e}")
        return []
