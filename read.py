def read_txt(path):
    text = ""
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    return text
