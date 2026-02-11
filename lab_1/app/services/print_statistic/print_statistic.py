from statistics import median
from collections import Counter


def print_statistic(texts: list[str], tokens: list[list[str]]) -> None:
    """
    Выводит статистику по текстам:
    - Количество текстов
    - Средняя и медианная длины предложений (в словах)
    - Средняя и медианная длины слов (в символах)
    - Минимальная и максимальная длины предложений
    - Минимальная и максимальная длины слов
    - Количество уникальных слов
    """

    # Количество текстов
    num_texts = len(texts)

    # Длины предложений в словах
    sentence_lengths = [len(token_list) for token_list in tokens]

    # Все слова из всех текстов
    all_words = []
    for token_list in tokens:
        all_words.extend(token_list)

    # Длины слов в символах
    word_lengths = [len(word) for word in all_words]

    # Уникальные слова
    unique_words = set(all_words)
    num_unique_words = len(unique_words)

    # Вычисления
    avg_sentence_length = (
        sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    )
    median_sentence_length = median(sentence_lengths) if sentence_lengths else 0

    min_sentence_length = min(sentence_lengths) if sentence_lengths else 0
    max_sentence_length = max(sentence_lengths) if sentence_lengths else 0

    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    median_word_length = median(word_lengths) if word_lengths else 0

    min_word_length = min(word_lengths) if word_lengths else 0
    max_word_length = max(word_lengths) if word_lengths else 0

    # Вывод статистики
    print("=" * 70)
    print("СТАТИСТИКА ПО ТЕКСТАМ")
    print("=" * 70)
    print(f"\nКоличество текстов: {num_texts}")
    print(f"\nКоличество уникальных слов: {num_unique_words}")
    print(f"Общее количество слов: {len(all_words)}")

    print("\n" + "-" * 70)
    print("СТАТИСТИКА ПО ПРЕДЛОЖЕНИЯМ (в словах):")
    print("-" * 70)
    print(f"Средняя длина предложения: {avg_sentence_length:.2f} слов")
    print(f"Медианная длина предложения: {median_sentence_length} слов")
    print(f"Минимальная длина предложения: {min_sentence_length} слов")
    print(f"Максимальная длина предложения: {max_sentence_length} слов")

    print("\n" + "-" * 70)
    print("СТАТИСТИКА ПО СЛОВАМ (в символах):")
    print("-" * 70)
    print(f"Средняя длина слова: {avg_word_length:.2f} символов")
    print(f"Медианная длина слова: {median_word_length} символов")
    print(f"Минимальная длина слова: {min_word_length} символов")
    print(f"Максимальная длина слова: {max_word_length} символов")
    print("=" * 70)
