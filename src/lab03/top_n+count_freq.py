def count_freq(tokens: list[str]) -> dict[str, int]:
    # Использую словарь для подсчета количества одинаковых слов
    freq_dict = {}

    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1

    return freq_dict


print(f" Промежуточный {count_freq(["a","b","a","c","b","a"])}")


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
print(top_n(freq2, 3))
