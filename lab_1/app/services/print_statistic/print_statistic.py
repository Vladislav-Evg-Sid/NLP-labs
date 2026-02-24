import statistics
from typing import Iterable, Sequence, Union
from collections import Counter
import pymorphy3


def _is_word(token: str) -> bool:
    return any(ch.isalpha() for ch in token)


# Morph analyzer for POS tagging
morph = pymorphy3.MorphAnalyzer()

# Mapping POS tags to Russian names
POS_RU = {
    "NOUN": "Существительное",
    "VERB": "Глагол",
    "INFN": "Инфинитив",
    "ADJF": "Прилагательное (полное)",
    "ADJS": "Прилагательное (краткое)",
    "COMP": "Сравнительная степень",
    "PRTF": "Причастие (полное)",
    "PRTS": "Причастие (краткое)",
    "GRND": "Деепричастие",
    "NUMR": "Числительное",
    "ADVB": "Наречие",
    "NPRO": "Местоимение",
    "PRED": "Предикатив",
    "PREP": "Предлог",
    "CONJ": "Союз",
    "PRCL": "Частица",
    "INTJ": "Междометие",
    "UNDEFINED": "Неопределённая часть речи",
}


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


def print_statistic(data: list[tuple[list[list[str]], list[str]]]) -> None:
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
            all_word_count: int = 0

            for sent_lists, flat in token_texts:
                for s in sent_lists:
                    sentence_lengths.append(len([w for w in s if _is_word(w)]))
                all_word_count += len(flat)
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
            
            print(f"\nКоэффициент лексического разнообразия: {len(unique_words)/all_word_count}")
            
            print("\nВыполняется частотный анализ частей речи...")
            pos_counts: Counter = Counter()
            for _, flat_tokens in token_texts:
                for w in flat_tokens:
                    if not _is_word(w):
                        continue
                    try:
                        p = morph.parse(w)[0]
                        pos = p.tag.POS or "UNDEFINED"
                    except Exception:
                        pos = "UNDEFINED"
                    pos_counts[pos] += 1

            total_tokens = all_word_count if all_word_count > 0 else sum(pos_counts.values())
            print("Частотный анализ частей речи:")
            for pos, cnt in pos_counts.most_common():
                label = POS_RU.get(pos, pos if pos is not None else "UNDEFINED")
                if label == "UNDEFINED":
                    label = POS_RU["UNDEFINED"]
                print(f" {label}: {cnt} ({cnt/total_tokens:.2%})")
            return

    print("Входные данные имеют неизвестную форму для вычисления статистики")
