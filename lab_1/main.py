from app.services.loader.loader import parce_file
from app.services.loader.load_official_parts_of_speech import load_official_parts_of_speech
from app.services.loader.csv_parcer import parce_csv_by_categories
from app.services.clean_up_text.clean_up_text import clean_up_text
from app.services.tokenize.tokenize import tokenize
from app.services.normalize.normalize import normalize, NormalizeType
from app.services.print_statistic.print_statistic import print_statistic
from app.services.visualization.visualization import create_both


FILE_PATH = "C:/git/NLP-labs/lab_1/data/"

def conveyor_belt_processing(texts: list[str]) -> list[tuple[list[list[str]], list[str]]]:
    """Обрабатывает тексты

    Args:
        texts (list[str]): Корпус текстов
        official_parts (set[str]): Вспомогательные части речи

    Returns:
        list[tuple[list[list[str]], list[str]]]: Токены
    """    
    official_parts = load_official_parts_of_speech(
        FILE_PATH + "служебные части речи.txt"
    )
    print("Служебные части речи получены")
    
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
    normalized_tokens = conveyor_belt_processing(texts)
    
    print_statistic(normalized_tokens)


def processing_tokens(texts_by_categories: dict[str, list[str]]) -> tuple[dict[str, dict[str, int]], dict[str, list[tuple[list[list[str]], list[str]]]]]:
    frequencies_by_categories = dict()
    normalized_tokens = dict()
    
    for category in texts_by_categories.keys():
        norm_tokens = conveyor_belt_processing(texts_by_categories[category])
        normalized_tokens[category] = norm_tokens
        frequencies = dict()
        for cur_token in norm_tokens[0][1]:
            frequencies_by_token = 0
            for text in texts_by_categories[category]:
                frequencies_by_token += text.count(cur_token)
            frequencies[cur_token] = frequencies_by_token
        frequencies_by_categories[category] = frequencies
    return frequencies_by_categories, normalized_tokens


def vizualization_plots(frequencies_by_categories: dict[str, dict[str, int]]) -> None:
    for category, frequencies in frequencies_by_categories.items():
        create_both(
            frequencies,
            count_words_to_visualization_hist=40,
            count_words_to_visualization_wc=100,
            window_name=f"Анализ частотности токенов по теме: \"{category}\""
        )
    input("Процесс выполнен")


def main() -> None:
    """Основной код для решения домашней работы
    """
    texts_by_categories = parce_csv_by_categories(file_path=FILE_PATH+"news_5k.csv")
    frequencies_by_categories, norm_texts_by_categories = processing_tokens(texts_by_categories)
    # vizualization_plots(frequencies_by_categories)
    for category, norm_texts in norm_texts_by_categories.items():
        print("\tКатегория:", category)
        print_statistic(norm_texts)

if __name__ == "__main__":
    main()
