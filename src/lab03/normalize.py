def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    for i in '\n\t\r':
        text = text.replace(i," ")
    if yo2e==True:
        text = text.replace("ё","е").replace("Ё","Е")
    if casefold:
        text = text.casefold()
    while "  " in text:
        text = text.replace("  ", " ")
    return text.strip()
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные  пробелы  "))