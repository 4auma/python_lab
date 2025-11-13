# normilaze
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
# Вывод:
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize 
def tokenize(text: str) -> list[str]:
    for i in ",!:😀":
        text=text.replace(i,"")
    text=text.strip()
    text=text.split()
    return text
# Вывод:
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]
assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

# count_freq.py
def count_freq(tokens: list[str]) -> dict[str, int]:
    f=[]
    d=[]
    g=[]
    k=set(tokens)
    for i in k:
       m=tokens.count(i)
       g.append(f"{i}:{m}")
       k=g[:2]
    return f" Частота {sorted(g)}",f" Топ - 2 слов {sorted(k)}"
# Вывод:
assert count_freq(["a","b","a","c","b","a"]) == (" Частота ['a:3', 'b:2', 'c:1']", " Топ - 2 слов ['a:3', 'b:2']")

# top_n+count_freq.py
def count_freq(tokens: list[str]) -> dict[str, int]:
    # Использую словарь для подсчета количества одинаковых слов
    freq_dict={}
    
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
# Вывод:
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]