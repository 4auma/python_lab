def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio = fio.split()
    stroka = []
    for name in fio[1:]:
        i = f"{name[0].upper()}."
        stroka.append(i) 
    formatted_fio = f"{fio[0]} {' '.join(stroka)}"
    formatted_gpa = f"{gpa:.2f}"
    result = f"{formatted_fio}, гр. {group}, GPA {formatted_gpa}"
    return result
s=("Петров Пётр", "IKBO-12", 5.0)
f=format_record(s)
print(f)
print(stroka)