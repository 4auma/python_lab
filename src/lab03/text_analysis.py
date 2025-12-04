import re
from collections import Counter

def read_text_file(file_path):
    """Чтение текстового файла"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_word_frequencies(text, top_n=5):
    """Получение частотности слов"""
    # Убираем пунктуацию и приводим к нижнему регистру
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(top_n)