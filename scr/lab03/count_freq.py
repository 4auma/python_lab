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
print(count_freq(["a","b","a","c","b","a"]))
