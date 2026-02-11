import statistics
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from typing import Iterable, Sequence, Union


# Ensure punkt is available (tokenize.py also downloads it; harmless if repeated)
nltk.download("punkt", quiet=True)


def _is_word(token: str) -> bool:
    return any(ch.isalpha() for ch in token)


def _safe_stats(values: Iterable[int]) -> tuple[float, float, int, int]:
    vals = list(values)
    if not vals:
        return 0.0, 0.0, 0, 0
    return (
        statistics.mean(vals),
        statistics.median(vals),
        min(vals),
        max(vals),
    )


def print_statistic(
    data: Union[Sequence[str], Sequence[Sequence[str]]]
) -> None:
    if not data:
        print("----- Статистика текстов -----")
        print("Количество текстов: 0")
        return

    if all(isinstance(x, Sequence) for x in data):
        is_norm_by_sentence = all(
            isinstance(x, Sequence)
            and len(x) >= 2
            and all(isinstance(s, Sequence) for s in x[0])
            for x in data
        )

        if is_norm_by_sentence:
            token_texts = data
            num_texts = len(token_texts)

            sentence_lengths: list[int] = []
            word_lengths: list[int] = []
            unique_words: set[str] = set()

            for sent_lists, flat in token_texts:
                for s in sent_lists:
                    sentence_lengths.append(len([w for w in s if _is_word(w)]))
                for w in flat:
                    if _is_word(w):
                        word_lengths.append(len(w))
                        unique_words.add(w.lower())

            avg_sent, med_sent, min_sent, max_sent = _safe_stats(sentence_lengths)
            avg_word, med_word, min_word, max_word = _safe_stats(word_lengths)

            
            print("----- Статистика текстов -----")
            print(f"Количество текстов: {num_texts}")

            print("\nДлина предложений (в словах):")
            print(f"Среднее: {avg_sent:.2f}")
            print(f"Медиана: {med_sent:.2f}")
            print(f"Минимальная: {min_sent}")
            print(f"Максимальная: {max_sent}")

            print("\nДлина слов (в символах):")
            print(f"Среднее: {avg_word:.2f}")
            print(f"Медиана: {med_word:.2f}")
            print(f"Минимальная: {min_word}")
            print(f"Максимальная: {max_word}")

            print(f"\nКоличество уникальных слов во всех текстах: {len(unique_words)}\n")
            return

    print("Входные данные имеют неизвестную форму для вычисления статистики")
