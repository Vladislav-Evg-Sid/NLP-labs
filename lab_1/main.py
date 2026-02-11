from app.services.loader.loader import parce_file
from app.services.loader.load_official_parts_of_speech import (
    load_official_parts_of_speech,
)
from app.services.clean_up_text.clean_up_text import clean_up_text
from app.services.tokenize.tokenize import tokenize
from app.services.normalize.normalize import normalize, NormalizeType
from app.services.print_statistic.print_statistic import print_statistic


def main() -> None:
    file_path = "C:/git/NLP-labs/lab_1/data/"
    file_name = input("Введите название файла: ")
    texts = parce_file(file_path + file_name)
    print("Тексты получены")
    official_parts = load_official_parts_of_speech(
        file_path + "служебные части речи.txt"
    )
    print("Служебные части речи получены")
    cleaned_texts = clean_up_text(texts)
    print("Текст очищен")

    tokens = tokenize(cleaned_texts)
    print("Текст токенизирован")
    normalized_tokens = normalize(tokens, official_parts, NormalizeType.LEMMATIZE)
    print("Текст нормализован")
    
    print_statistic(normalized_tokens)


if __name__ == "__main__":
    main()
