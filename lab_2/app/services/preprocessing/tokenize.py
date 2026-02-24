from __future__ import annotations
import nltk
from pandas import Series


nltk.download("averaged_perceptron_tagger_eng")
from nltk import pos_tag


def tokenizer(texts: Series[str]) -> Series[list[tuple[str, str]]]:
    texts = texts.copy()
    return texts.apply(lambda x: pos_tag(x.split(" ")))
