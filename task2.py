# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)



def index_num(array, min_num, max_num):
    mas = []
    for i in range(len(array)):
        if arr[i] >= min_num and arr[i] <= max_num:
            mas.append(array[i])
    return mas

min_num = int(input('введите минимум: '))
max_num = int(input('введите максимум: '))
array = input("Введите элементы массива через пробел: ").split()
arr = [int(x) for x in array]

mas = index_num(array, min_num, max_num)

for index in mas:
    print(index)

