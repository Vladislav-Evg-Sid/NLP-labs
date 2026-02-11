import docx


def parse_docx(file_path: str) -> list[str]:
    try:
        doc = docx.Document(file_path)
        full_text = []

        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                full_text.append(paragraph.text)

        combined_text = " ".join(full_text)
        separated_texts = [
            text.strip() for text in combined_text.split("SEP") if text.strip()
        ]

        return separated_texts
    except Exception as e:
        print(f"Ошибка при парсинге DOCX файла {file_path}: {e}")
        return []
