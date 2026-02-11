from app.services.loader import csv_parcer, pdf_parcer, docx_parcer, txt_parcer


def parce_file(file_path: str) -> list[str]:
    temp = file_path.split(".")
    if len(temp) < 1:
        print("Нет расширения искомого файла")
        return []
    file_type = temp[-1].lower()
    match file_type:
        case "pdf":
            return pdf_parcer.parse_pdf(file_path)
        case "docx":
            return docx_parcer.parse_docx(file_path)
        case "txt":
            return txt_parcer.parse_txt(file_path)
        case "csv":
            return csv_parcer.parse_csv(file_path)
    print("Некорректный тип файла")
    return []
