def parse_txt(file_path: str, encoding: str = "utf-8") -> list[str]:
    try:
        with open(file_path, "r", encoding=encoding) as file:
            content = file.read()

        separated_texts = [
            text.strip() for text in content.split("SEP") if text.strip()
        ]

        return separated_texts
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="cp1251") as file:
                content = file.read()
            separated_texts = [
                text.strip() for text in content.split("SEP") if text.strip()
            ]
            return separated_texts
        except Exception as e:
            print(f"Ошибка кодировки при парсинге TXT файла {file_path}: {e}")
            return []
    except Exception as e:
        print(f"Ошибка при парсинге TXT файла {file_path}: {e}")
        return []
