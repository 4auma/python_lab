"""
Модуль для работы с текстом из ЛР3
"""

import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализует текст."""
    for char in "\n\t\r":
        text = text.replace(char, " ")

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    if casefold:
        text = text.casefold()

    while "  " in text:
        text = text.replace("  ", " ")

    return text.strip()


def tokenize(text: str) -> list[str]:
    """Токенизирует нормализованный текст."""
    # Просто разбиваем по пробелам - для русского текста этого достаточно
    return [word for word in text.split() if word]


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту слов."""
    freq_dict = {}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Возвращает топ-N самых частых слов."""
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует словарь частот."""
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
