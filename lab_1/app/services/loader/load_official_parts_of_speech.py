def load_official_parts_of_speech(file_path: str) -> set[str]:
    result = set()
    with open(file_path, "r", encoding="utf-8") as file:
        s = file.readline()
        while s != "":
            result.add(s)
            s = file.readline()
    return result
