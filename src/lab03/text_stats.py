def text_stats(tokens: list[str]) -> dict[str, int]:
    h = []
    g = []
    p = []
    for i in "!,.":
        tokens = tokens.replace(i, " ")
    s = tokens.split()
    for i in s:
        g.append(i)
        f = set(g)
    for i in f:
        m = tokens.count(i)
        p.append(f"{i}:{m}")
    k = p
    r = [i.split(":") for i in k]
    for i in r:
        l = i[-1], i[:1]
        h.append([l])
    return f"Всего слов - {len(g)}", f"Уникальных слов - {len(p)}", f" Топ слов - {(h)}"


print(text_stats("Привет, ура, ура Привет Привет !!!"))
