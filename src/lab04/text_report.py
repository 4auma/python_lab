#!/usr/bin/env python3
"""
Скрипт для генерации отчета по статистике слов в тексте
"""

import argparse
import sys
from pathlib import Path

# Добавляем корневую папку в Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Теперь импортируем наши модули
from src.lib.text import normalize, tokenize, count_freq, top_n, sorted_word_counts
from src.lab04.io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    """Вычисляет частоты слов из текста."""
    tokens = tokenize(normalize(text))
    return count_freq(tokens)


def generate_report(input_file: str, output_file: str) -> None:
    """Генерирует отчет по словам из входного файла."""
    # Читаем текст из файла
    text = read_text(input_file)
    
    # Вычисляем частоты
    freq = frequencies_from_text(text)
    
    # Сортируем слова по частоте
    sorted_words = sorted_word_counts(freq)
    
    # Записываем в CSV
    write_csv(sorted_words, output_file, header=("word", "count"))
    
    # Выводим статистику в консоль
    total_words = sum(freq.values())
    unique_words = len(freq)
    top_5 = top_n(freq, 5)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5 слов:")
    for word, count in top_5:
        print(f"  {word}: {count}")
    
    print(f"\nОтчет сохранен в: {output_file}")


def main():
    """Основная функция скрипта."""
    parser = argparse.ArgumentParser(description='Генерация отчета по статистике слов')
    parser.add_argument('--in', dest='input_file', default='data/lab04/input.txt',
                       help='Входной текстовый файл')
    parser.add_argument('--out', dest='output_file', default='data/lab04/report.csv',
                       help='Выходной CSV файл')
    
    args = parser.parse_args()
    
    # Проверяем существование входного файла
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Ошибка: Входной файл '{args.input_file}' не найден")
        print(f"Полный путь: {input_path.absolute()}")
        return
    
    generate_report(args.input_file, args.output_file)


if __name__ == "__main__":
    main()