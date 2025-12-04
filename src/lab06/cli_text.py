import argparse
import os
import sys
import re
from collections import Counter

def get_absolute_path(relative_path):
    """Получить абсолютный путь к файлу, ища в data/samples"""
    # Если передан абсолютный путь или файл существует
    if os.path.isabs(relative_path) or os.path.exists(relative_path):
        return relative_path
    
    # Вариант 1: Ищем в src/data/samples/
    src_data_path = os.path.join("src", "data", "samples", relative_path)
    if os.path.exists(src_data_path):
        return src_data_path
    
    # Вариант 2: Ищем в data/samples (относительно текущей директории)
    data_path = os.path.join("data", "samples", relative_path)
    if os.path.exists(data_path):
        return data_path
    
    # Вариант 3: Ищем в текущей директории проекта
    project_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "samples", relative_path)
    if os.path.exists(project_path):
        return project_path
    
    return relative_path  # Вернём как есть, будет ошибка при открытии

def cat_command(input_file, number_lines=False):
    """Вывести содержимое файла"""
    full_path = get_absolute_path(input_file)
    
    if not os.path.exists(full_path):
        print(f"❌ Ошибка: файл '{input_file}' не найден")
        print(f"   Искали по пути: {full_path}")
        return
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines, 1):
                if number_lines:
                    print(f"{i:4}: {line.rstrip()}")
                else:
                    print(line.rstrip())
    except Exception as e:
        print(f"❌ Ошибка чтения файла: {e}")

def stats_command(input_file, top_n=5):
    """Анализ частотности слов"""
    full_path = get_absolute_path(input_file)
    
    if not os.path.exists(full_path):
        print(f"❌ Ошибка: файл '{input_file}' не найден")
        print(f"   Искали по пути: {full_path}")
        return
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        words = re.findall(r'\b\w+\b', text.lower())
        word_counts = Counter(words)
        
        print(f"📊 Топ-{top_n} слов в файле '{input_file}':")
        print("─" * 40)
        for word, count in word_counts.most_common(top_n):
            print(f"{word:20} : {count:3}")
        print("─" * 40)
        print(f"Всего слов: {len(words)}")
        print(f"Уникальных слов: {len(word_counts)}")
        
    except Exception as e:
        print(f"❌ Ошибка анализа файла: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для лабораторной работы №6",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
📋 Примеры использования:
  
  # Используйте относительные пути:
  python cli_text.py cat --input people.txt -n
  
  # Или полные пути:
  python cli_text.py cat --input src/data/samples/people.txt -n
  
  python cli_text.py stats --input people.txt --top 10
  
💡 Совет: Файлы ищутся в папке src/data/samples/
        """
    )
    
    subparsers = parser.add_subparsers(
        dest="command",
        help="Доступные команды",
        required=True
    )
    
    # Команда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Входной файл (можно указать просто имя файла из src/data/samples/)")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки при выводе")
    
    # Команда stats
    stats_parser = subparsers.add_parser("stats", help="Анализ частотности слов")
    stats_parser.add_argument("--input", required=True, help="Текстовый файл для анализа")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов (по умолчанию: 5)")
    
    args = parser.parse_args()
    
    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)

if __name__ == "__main__":
    main()