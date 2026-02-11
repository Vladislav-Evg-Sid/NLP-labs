import PyPDF2


def parse_pdf(file_path: str) -> list[str]:
    try:
        pdf_text = []

        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text.strip():
                    pdf_text.append(text)

        combined_text = " ".join(pdf_text)
        separated_texts = [
            text.strip() for text in combined_text.split("SEP") if text.strip()
        ]

        return separated_texts
    except Exception as e:
        print(f"Ошибка при парсинге PDF файла {file_path}: {e}")
        return []
