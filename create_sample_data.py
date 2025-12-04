import json
import csv
import os

print("Создание тестовых данных для лабораторной работы №6...")

# Определяем путь к src/data/
data_dir = os.path.join("src", "data")
samples_dir = os.path.join(data_dir, "samples")
out_dir = os.path.join(data_dir, "out")

# Создаем директории
os.makedirs(samples_dir, exist_ok=True)
os.makedirs(out_dir, exist_ok=True)

# 1. Создаем JSON файл
people_json = [
    {"name": "Иван Иванов", "age": 25, "city": "Москва", "occupation": "Инженер"},
    {"name": "Мария Петрова", "age": 30, "city": "Санкт-Петербург", "occupation": "Врач"},
    {"name": "Алексей Сидоров", "age": 22, "city": "Казань", "occupation": "Студент"},
    {"name": "Елена Кузнецова", "age": 28, "city": "Новосибирск", "occupation": "Учитель"},
    {"name": "Дмитрий Смирнов", "age": 35, "city": "Екатеринбург", "occupation": "Программист"}
]

json_path = os.path.join(samples_dir, "people.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(people_json, f, ensure_ascii=False, indent=2)
print(f"✅ Создан: {json_path}")

# 2. Создаем CSV файл
csv_path = os.path.join(samples_dir, "people.csv")
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city", "occupation"])
    writer.writeheader()
    writer.writerows(people_json)
print(f"✅ Создан: {csv_path}")

# 3. Создаем текстовый файл для анализа
txt_path = os.path.join(samples_dir, "people.txt")
text_content = """Иван работает в Москве. Мария живет в Санкт-Петербурге.
Алексей учится в Казани. Елена работает в Новосибирске.
Дмитрий работает в Екатеринбурге. Иван и Мария друзья.
Москва и Санкт-Петербург - крупные города России.
Иван часто бывает в Москве и Санкт-Петербурге.
Программист Дмитрий создает полезные программы.
Врач Мария помогает людям в больнице.
Учитель Елена преподает в школе.
Инженер Иван проектирует новые здания."""

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(text_content)
print(f"✅ Создан: {txt_path}")

print("\n" + "="*60)
print("🎉 Тестовые данные успешно созданы!")
print("="*60)
print(f"\n📁 Структура создана:")
print(f"   {samples_dir}/")
print(f"     ├── people.json")
print(f"     ├── people.csv")
print(f"     └── people.txt")
print(f"   {out_dir}/")
print(f"     └── (здесь будут результаты)")
print("\n🚀 Команды для тестирования:")
print("   python src\\lab06\\cli_text.py cat --input people.txt -n")
print("   python src\\lab06\\cli_text.py stats --input people.txt --top 5")
print("   python src\\lab06\\cli_convert.py json2csv --in people.json --out result.csv")
print("   python src\\lab06\\cli_convert.py csv2json --in people.csv --out result.json")
print("   python src\\lab06\\cli_convert.py csv2xlsx --in people.csv --out result.xlsx")
print("\n💡 Подсказка: Можно указывать просто имена файлов,")
print("   они автоматически найдутся в src/data/samples/")