import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое как строку.

    Args:
        path: Путь к файлу
        encoding: Кодировка файла (по умолчанию UTF-8)

    Returns:
        Содержимое файла как строка

    Raises:
        FileNotFoundError: Если файл не существует
        UnicodeDecodeError: Если возникли проблемы с декодированием

    Examples:
        >>> text = read_text("data/input.txt")
        >>> text = read_text("data/input.txt", encoding="cp1251")
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Записывает данные в CSV файл.

    Args:
        rows: Итерируемый объект с данными для записи
        path: Путь для сохранения CSV файла
        header: Заголовок столбцов (опционально)

    Raises:
        ValueError: Если строки имеют разную длину

    Examples:
        >>> write_csv([("word", "count"), ("test", 3)], "data/report.csv")
        >>> write_csv([], "empty.csv", header=("col1", "col2"))
    """
    p = Path(path)
    rows_list = list(rows)

    # Проверяем одинаковую длину всех строк
    if rows_list:
        first_len = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_len:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, ожидалась {first_len}"
                )

    # Создаем родительские директории если нужно
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)


def ensure_parent_dir(path: str | Path) -> None:
    """
    Создает родительские директории для указанного пути если они не существуют.

    Args:
        path: Путь к файлу
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
