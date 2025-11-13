import os
import csv
import sys
from pathlib import Path
from typing import Iterable, Sequence
from openpyxl import Workbook

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    # Проверка существования файла с помощью Path
    p = Path(csv_path)
    if not p.exists():
        print("FileNotFoundError")
        sys.exit(1)

    # Проверка что файл не пустой
    if p.stat().st_size == 0:
        print("ValueError")
        sys.exit(1)

    # Создание Excel-книги
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    # Чтение CSV файла с использованием pathlib
    with p.open("r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            ws.append(row)

    # Настройка ширины колонок
    for column_cells in ws.columns:
        max_length = 0
        column_letter = column_cells[0].column_letter
        for cell in column_cells:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8)
    
    # Сохранение с использованием Path
    xlsx_p = Path(xlsx_path)
    wb.save(xlsx_p)

# Дополнительные функции для работы с текстом (если понадобятся)
from collections import Counter

def frequencies_from_text(text: str) -> dict[str, int]:
    # Импорты внутри функции чтобы избежать циклических зависимостей
    from lib.text import normalize, tokenize  # из ЛР3
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

# Пример использования
if __name__ == "__main__":
    # Используем Path для путей
    csv_path = Path(r"C:\Users\darin\Documents\GitHub\Лабораторная Работа №1\date\samples\cities.csv")
    xlsx_path = Path(r"C:\Users\darin\Documents\GitHub\Лабораторная Работа №1\date\out\people.xlsx")
    
    csv_to_xlsx(csv_path, xlsx_path)
    
    # Дополнительный пример: чтение CSV как текста и анализ
    try:
        csv_text = read_text(csv_path)
        print(f"CSV файл прочитан, размер: {len(csv_text)} символов")
        
        # Если нужно проанализировать содержимое
        # freq = frequencies_from_text(csv_text)
        # sorted_counts = sorted_word_counts(freq)
        # print("Топ-10 самых частых слов:", sorted_counts[:10])
        
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")