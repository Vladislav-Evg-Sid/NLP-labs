from nltk import download as nltk_download
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import pymorphy3
from enum import Enum
from nltk.tokenize import word_tokenize


def _is_word(token: str) -> bool:
    return any(ch.isalpha() for ch in token)

# Скачивание необходимых ресурсов NLTK
nltk_download("stopwords")
russian_stopwords = stopwords.words("russian")
stemmer = SnowballStemmer("russian")
morph = pymorphy3.MorphAnalyzer()


class NormalizeType(Enum):
    STEMMING = "stemming"
    LEMMATIZE = "lemmatize"


def add_stopwords(base: list[str], dop: set[str]) -> set[str]:
    base_set = set(w.lower() for w in base)
    dop_set = set(w.lower() for w in dop)
    all_stopwords = base_set | dop_set
    return all_stopwords


def delete_stop_words(tokens: list[list[str]], stop_words: set[str]) -> None:
    for i in range(len(tokens)):
        for sw in stop_words:
            try:
                tokens[i].remove(sw)
            except:
                pass


def stem_text(tokens: list[str]) -> list[str]:
    return [stemmer.stem(word) for word in tokens]


def lemmatize_text(tokens: list[str]) -> list[str]:
    lemmas = []
    for word in tokens:
        # Анализ слова и выбор наиболее вероятной формы
        parsed = morph.parse(word)[0]
        lemmas.append(parsed.normal_form)
    return lemmas


def normalize(
    tokens: list[list[str]],
    dop_stop_words: set[str] | None = None,
    norm_type: NormalizeType = NormalizeType.LEMMATIZE,
) -> list[tuple[list[list[str]], list[str]]]:
    if dop_stop_words is None:
        dop_stop_words = set()
    stop_words = add_stopwords(russian_stopwords, dop_stop_words)
    match norm_type:
        case NormalizeType.LEMMATIZE:
            result: list = []
            for tok in tokens:
                if isinstance(tok, (list, tuple)) and len(tok) >= 1:
                    sentences = tok[0]
                else:
                    sentences = []

                sentence_lemmas: list[list[str]] = []
                for sent in sentences:
                    sent_words = [w for w in word_tokenize(sent, language="russian") if _is_word(w)]
                    lemmas = lemmatize_text(sent_words)
                    filtered = [l for l in lemmas if l.lower() not in stop_words]
                    sentence_lemmas.append(filtered)

                flat = [w for s in sentence_lemmas for w in s]
                result.append((sentence_lemmas, flat))
            return result
        case NormalizeType.STEMMING:
            result: list = []
            for tok in tokens:
                if isinstance(tok, (list, tuple)) and len(tok) >= 1:
                    sentences = tok[0]
                else:
                    sentences = []

                sentence_stems: list[list[str]] = []
                for sent in sentences:
                    sent_words = [w for w in word_tokenize(sent, language="russian") if _is_word(w)]
                    stems = stem_text(sent_words)
                    lemmas_for_check = lemmatize_text(sent_words)
                    filtered_stems = [s for s, l in zip(stems, lemmas_for_check) if l.lower() not in stop_words and s.lower() not in stop_words]
                    sentence_stems.append(filtered_stems)

                flat = [w for s in sentence_stems for w in s]
                result.append((sentence_stems, flat))
            return result
    return []
