import argparse
import os
import sys
import json
import csv

def get_input_path(file_path):
    """Получить путь к входному файлу"""
    if os.path.isabs(file_path) or os.path.exists(file_path):
        return file_path
    
    # Ищем в src/data/samples/
    paths_to_check = [
        os.path.join("src", "data", "samples", file_path),
        os.path.join("data", "samples", file_path),
        os.path.join("samples", file_path),
        os.path.join(os.path.dirname(__file__), "..", "..", "data", "samples", file_path)
    ]
    
    for path in paths_to_check:
        if os.path.exists(path):
            return path
    
    return file_path

def get_output_path(file_path):
    """Получить путь для выходного файла"""
    if os.path.isabs(file_path):
        return file_path
    
    # Если указан только имя файла, сохраняем в src/data/out/
    if "/" not in file_path and "\\" not in file_path:
        return os.path.join("src", "data", "out", file_path)
    
    return file_path

def json_to_csv(input_file, output_file):
    """Конвертирует JSON файл в CSV"""
    input_path = get_input_path(input_file)
    output_path = get_output_path(output_file)
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Файл {input_file} не найден (искали: {input_path})")
    
    # Создаем папку для выходного файла
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    if isinstance(data, list) and len(data) > 0:
        fieldnames = data[0].keys()
        with open(output_path, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    else:
        raise ValueError("Неверный формат JSON данных")

def csv_to_json(input_file, output_file):
    """Конвертирует CSV файл в JSON"""
    input_path = get_input_path(input_file)
    output_path = get_output_path(output_file)
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Файл {input_file} не найден (искали: {input_path})")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)

def csv_to_xlsx(input_file, output_file):
    """Конвертирует CSV файл в XLSX"""
    input_path = get_input_path(input_file)
    output_path = get_output_path(output_file)
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Файл {input_file} не найден (искали: {input_path})")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        from openpyxl import Workbook
    except ImportError:
        print("❌ Ошибка: Для конвертации в XLSX установите openpyxl:")
        print("   pip install openpyxl")
        return
    
    wb = Workbook()
    ws = wb.active
    
    with open(input_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            ws.append(row)
    
    wb.save(output_path)

def main():
    parser = argparse.ArgumentParser(
        description="Конвертеры данных между форматами",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
📋 Примеры использования:
  
  # Просто имена файлов (будут искаться в src/data/samples/)
  python cli_convert.py json2csv --in people.json --out result.csv
  
  # Полные пути
  python cli_convert.py json2csv --in src/data/samples/people.json --out src/data/out/people.csv
  
  python cli_convert.py csv2json --in people.csv --out result.json
  python cli_convert.py csv2xlsx --in people.csv --out result.xlsx
  
💡 Совет: Входные файлы ищутся в src/data/samples/
         Выходные файлы сохраняются в src/data/out/
        """
    )
    
    sub = parser.add_subparsers(
        dest="cmd",
        help="Тип конвертации",
        required=True
    )
    
    # Подкоманда json2csv
    p1 = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")
    
    # Подкоманда csv2json
    p2 = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")
    
    # Подкоманда csv2xlsx
    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")
    
    args = parser.parse_args()
    
    try:
        if args.cmd == "json2csv":
            json_to_csv(args.input, args.output)
            print(f"✅ Успешно конвертирован: {args.input} → {args.output}")
        
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.output)
            print(f"✅ Успешно конвертирован: {args.input} → {args.output}")
        
        elif args.cmd == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
            print(f"✅ Успешно конвертирован: {args.input} → {args.output}")
        
    except FileNotFoundError as e:
        print(f"❌ Ошибка: {e}")
    except Exception as e:
        print(f"❌ Ошибка при конвертации: {e}")

if __name__ == "__main__":
    main()