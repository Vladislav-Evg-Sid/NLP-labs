def to_lower(texts: list[str]) -> list[str]:
    for i in range(len(texts)):
        texts[i] = texts[i].lower()
    return texts


def delete_number(texts: list[str]) -> list[str]:
    for i in range(len(texts)):
        for n in range(9):
            texts[i] = texts[i].replace(str(n), "")
    return texts


def delete_punct(texts: list[str]) -> list[str]:
    punct = [",", ";", ":", "'", '"', "(", ")"]
    for i in range(len(texts)):
        texts[i] = texts[i].replace(" - ", " ")
        for p in punct:
            texts[i] = texts[i].replace(p, "")
    return texts


def delete_spaces(texts: list[str]) -> list[str]:
    for i in range(len(texts)):
        while "  " in texts:
            texts[i] = texts[i].replace(" ", " ")
    return texts


def clean_up_text(input_texts: list[str]) -> list[str]:
    texts = input_texts.copy()
    texts = to_lower(texts)
    texts = delete_number(texts)
    texts = delete_punct(texts)
    texts = delete_spaces(texts)
    return texts
