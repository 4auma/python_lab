"""
import json, csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:

    json_file = Path("src/data/samples/people.json")

    if not json_file.exists():
        raise FileNotFoundError('Файл не найден')
    if json_file.suffix.lower() != '.json':
        raise ValueError('Не json')

    with open(json_path,'r', encoding='utf-8') as f:
        data_json = json.load(f)

    with open(csv_path,'w', encoding ='utf-8') as f:
        write = csv.DictWriter(f,fieldnames=data_json[0])
        write.writeheader()
        write.writerows(data_json)


def csv_to_json(csv_path: str, json_path: str) -> None:
    csv_file = Path("src/data/samples/people.csv")

    if not csv_file.exists():
        raise FileNotFoundError('Файл не найден')
    if csv_file.suffix.lower() != '.csv':
        raise ValueError('Не csv')

    with open(csv_path,'r',encoding ='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(json_path,'w',newline="",encoding = 'utf-8') as f:
        json.dump(data,f, ensure_ascii=False, indent=2)

"""

"""
csv_to_json("src/data/samples/people.csv","src/data/out/people_from_csv.json") 
json_to_csv("src/data/samples/people.json", "src/data/out/people_from_json.csv")
"""
import json
import csv
import os


def json_to_csv(input_file, output_file):
    """Конвертирует JSON файл в CSV"""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Файл {input_file} не найден")

    with open(input_file, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    # Если данные - список словарей
    if isinstance(data, list) and len(data) > 0:
        fieldnames = data[0].keys()
        with open(output_file, "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    else:
        raise ValueError("Неверный формат JSON данных")


def csv_to_json(input_file, output_file):
    """Конвертирует CSV файл в JSON"""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Файл {input_file} не найден")

    with open(input_file, "r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)

    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
