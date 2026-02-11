from nltk import download as nltk_download
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import pymorphy3
from enum import Enum

# Скачивание необходимых ресурсов NLTK
nltk_download("stopwords")
russian_stopwords = stopwords.words("russian")
stemmer = SnowballStemmer("russian")
morph = pymorphy3.MorphAnalyzer()


class NormalizeType(Enum):
    STEMMING = "stemming"
    LEMMATIZE = "lemmatize"


def add_stopwords(base: list[str], dop: set[str]) -> set[str]:
    all_stopwords = set(base) | dop
    return all_stopwords


def delete_stop_words(tokens: list[list[str]], stop_words: set[str]):
    for i in range(len(tokens)):
        for sw in stop_words:
            try:
                tokens[i].remove(sw)
            except:
                pass


def stem_text(tokens):  # TODO: Дописать сигнатуру
    return [stemmer.stem(word) for word in tokens]


def lemmatize_text(tokens):  # TODO: Дописать сигнатуру
    lemmas = []
    for word in tokens:
        # Анализ слова и выбор наиболее вероятной формы
        parsed = morph.parse(word)[0]
        lemmas.append(parsed.normal_form)
    return lemmas


def normalize(
    tokens: list[list[str]],
    dop_stop_words: set[str] = [],
    norm_type: NormalizeType = NormalizeType.LEMMATIZE,
):  # TODO: Дописать сигнатуру
    stop_words = add_stopwords(russian_stopwords, dop_stop_words)
    match norm_type:
        case NormalizeType.LEMMATIZE:
            result = []
            for tok in tokens:
                result.append(lemmatize_text(tok))
            return result
        case NormalizeType.STEMMING:
            result = []
            for tok in tokens:
                result.append(stem_text(tok))
            return result
    return []
