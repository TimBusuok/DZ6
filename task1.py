# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Введите первый элемент: '))
diff = int(input('Введите разность: '))
amount_num = int(input('Введите кол-во чисел: '))
array = []

for i in range(amount_num):
    ai = a + i * diff
    array.append(ai)

for i in array:
    print(i)


