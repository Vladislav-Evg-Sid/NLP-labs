from app.services.loader.loader import parce_file
from app.services.loader.load_official_parts_of_speech import load_official_parts_of_speech
from app.services.loader.csv_parcer import parce_csv_all
from app.services.clean_up_text.clean_up_text import clean_up_text
from app.services.tokenize.tokenize import tokenize
from app.services.normalize.normalize import normalize, NormalizeType
from app.services.print_statistic.print_statistic import print_statistic


FILE_PATH = "C:/git/NLP-labs/lab_1/data/"

def conveyor_belt_processing(texts: list[str], official_parts: set[str]) -> list[tuple[list[list[str]], list[str]]]:
    """Обрабатывает тексты

    Args:
        texts (list[str]): Корпус текстов
        official_parts (set[str]): Вспомогательные части речи

    Returns:
        list[tuple[list[list[str]], list[str]]]: Токены
    """    
    cleaned_texts = clean_up_text(texts)
    print("Текст очищен")
    
    tokens = tokenize(cleaned_texts)
    print("Текст токенизирован")
    normalized_tokens = normalize(tokens, official_parts, NormalizeType.STEMMING)
    print("Текст нормализован")
    return normalized_tokens


def conveyor_belt_all() -> None:
    """Основной конвейер, реализующий всё необходимое
    """
    file_name = input("Введите название файла: ")
    texts = parce_file(FILE_PATH + file_name)
    print("Тексты получены")
    official_parts = load_official_parts_of_speech(
        FILE_PATH + "служебные части речи.txt"
    )
    print("Служебные части речи получены")
    normalized_tokens = conveyor_belt_processing(texts, official_parts)
    
    print_statistic(normalized_tokens)


def main() -> None:
    """Основной код для решения домашней работы
    """
    df = parce_csv_all(file_path=FILE_PATH+"news_5k.csv")
    print(df["rubric"].unique()) # TODO: Доделать второе задание


if __name__ == "__main__":
    main()
