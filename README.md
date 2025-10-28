# **Лабораторная работа №1**
## Задание 1
```python
print(f'Привет {input()}! Через год тебе будет {int(input()) + 1}')
```
![image01](images/lab01/image01.png)
## Задание 2 
```python
a, b = float(input()), float(input())
print(f'sum: {a + b}; avg: {(a + b) / 2}')
```
Функция Float - служит для хранения типа данных с плавающей точкой 
![image02](images/lab01/image02.png)
## Задание 3 
```python
price = float(input())
discount = float(input())
vat = float(input())

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f'База после скидки: {base}')
print(f'НДС: {vat_amount}')
print(f'Итого к оплате: {total}')
```
В данном случае base - это цена при скидке, а vat_amount - Цена после скидки с учетом НДС
![image03](images/lab01/image03.png)
## Задание 4 
```python
min = int(input())
print(f'{min//60}:{min % 60}')
```
![image04](images/lab01/image04.png)
## Задание 5
```python
fio = input()
con = [i for i in fio if i != ' ']
ini = [g for g in con if g.isupper()]
print(f'Инициалы: {"".join(ini)}')
print(f'Длина (символов): {len(con)}')
```
В коде я расписал два генератора. 
Первый - con - служит для удаления пробелов в строке. Если при пробежке по строке, геник видит пробел, он исключает его из последовательности.
Второй - ini - Служит для определения символа, если символ заглавный, то он остается в строке. 
Функция isupper - служит для выявления заглавной буквы.
![image05](images/lab01/image05.png)
## Задание 6
```python
k = int(input())
och = 0
zaoch = 0
for i in range(0, k):
    n = (input().split())
    if 'True' in n:
        och += 1
    else:
        zaoch += 1
print(och, zaoch)
```
В данной задаче split - Разбивает введенные слова на элементы массива, после чего, с помощью генератора мы ищем подходящее слово в этом массиве.
![image06](images/lab01/image06.png)
## Задание 7
```python
N = input()
con = 1
name = ''
for i in range(0, len(N)):
    if N[i].isupper():
        name += N[i]
        for j in range(i, len(N)):
            if N[j].isnumeric():
                for k in range(j + 1, len(N), con):
                    name += N[k]
                break
            con += 1
print(name)
```
Функция isupper - ищет заглавную букву в моем массиве, с помощью нее нахожу первую букву зашифрованного сообщения.
Функция isnumeric - ищет число, в моем случае я пробегаюсь от первой буквы моего зашифрованного слова и заканчивая длинной строки, затрагивая все возможные символы. Если следующий символ не цифра, то в таком случае мой счетчик повышается на 1, в задаче прямым текстом сказано, что символы моего зашифрованного слова находятся на определнном расстоянии друг от друга, чем я и пользуюсь.
Если я нахожу цифру, следовательно следующий элемент после цифры - элемент моего зашифрованного слова. 
![image07](images/lab01/image07.png)
# **Лабораторная работа №2**
## Задание 1.1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        raise ValueError
    minimum=min(nums)
    maximum=max(nums)
    return (minimum,maximum)
f=[1.5, 2, 2.0, -3.1]
s=min_max(f)
print(s)
```
Функция представленная на экране - возвращает два элемента массива из массива в котором имеется n - ое количество элементов.
функция берет максимальный и минимальный элемент массива и возвращает их.
![arrays01](images/lab02/arrays01.png)
## Задание 1.2
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums)==0:
        raise ValueError
    return sorted(set(nums))
f=[1.0, 1, 2.5, 2.5, 0]
s=unique_sorted(f)
print(s)
```
В данной задаче, ключевым моментом функции является функция sorted - Она вовращает отсортированный список начиная от наименьшего числа в массиве и заканчивая максимальным. 
Также использовал функцию set - она удаляет из множества одинаковые символы.
![arrays02](images/lab02/arrays02.png)
## Задание 1.3
```python
def flat(mat: list[list | tuple]) -> list:
    result=[]
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError    
        for g in i:
            if isinstance(g, (list, tuple)):
                raise TypeError
            result.append(g)
    return result
s=[[1], [], [2, 3]]
s=flat(s)
print(s)
```
В данной задаче я использую два цикла на проверку моеих массивов в массиве, Первый цикл проверяет, является ли данный элемент массивом в массиве, второй же проверяет не является ли элмент массивом в последовательности массивов в массиве. Далее по истечению проверки я возвращаю в новый массив значения прошлых значений в массиве. Немного запутанно, но пишу для себя :)
![arrays03](images/lab02/arrays03.png)
## Задание 2.1
```python
def transpose(mat):
    if not mat:
        return []
    row_length = len(mat[0])
    for p in mat:
        if len(p) != row_length:
            raise ValueError
    r = []
    for i in range(len(mat[0])):
        g = []
        for p in mat:
            g.append(p[i])
        r.append(g)
    return r
print(transpose([[1,2],[3,4]]))
```
В данной задачи я использовал два цикла, первый применялся для разбиения чисел строки на столбцы, второй , для сложения элементов столбцов в строки. Если длинна матрицы не совпадает с длинной строки - то пишу еррор.
![matrix01](images/lab02/matrix01.png)
## Задание 2.2 
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    result = []
    for i in mat:
        if len(i)<=1:
            raise TypeError
        i = sum(i)
        result.append(float(i))
    return result
s= [
    [1,2,3],
    [4,5,6]
    ]
f=row_sums(s)
print(f)
```
Пробегаюсь по массивам в массиве, если длинна элементов моего массива меньше двух, то выдаю ошибку, т.к рваная. После чего провожу сумму каждого массива и записываю в новый.
![matrix02](images/lab02/matrix02.png)
## Задание 2.3
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    f = len(mat[0])
    for z in mat:
        if len(z) != f:
            raise ValueError
    r = len(mat)        
    k = len(mat[0])    
    a = [0.0] * k
    for col in range(k):      
        for row in range(r):  
            a[col] += mat[row][col]  
    
    return a
f=[[1,2,3],[4,5,6],[7,7,7]]
l=col_sums(f)
print(l)
```
Код пробегается по всем числам матрицы, начиная от mat[0][0] и заканчивая mat[n][m], Если длинна строки отличается от длинн остальных строк, то вывожу ошибку. Код работает с помощью цикла. Первый цикл, проходится по столбу, второй по строке, чтобы найти количество столбов я применяю функцию len(mat). когда второй цикл пробежится по всем числам строки, первый цикл поменяет индекс с [0]->[1] и так далее.
![matrix03](images/lab02/matrix03.png)
## Задание 3
```python
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
```
В своем коде я разбиваю ФИО на массив состоящий из трех элементов Ф,И,О Позже так будет проще искать нужные буквы. Создаю цикл с помощью которого пробегаюсь по имени и отчеству, с его помощи я беру первую букву Имени, и приписываю ее к фамилии. 
gpa:.2f - делает два знака после запятой. 
в результат записываю исзодную строку которая должна получится.
![typles01](images/lab02/typles01.png)
