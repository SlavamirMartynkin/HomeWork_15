# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_border = int(input('Ввелите нижнюю границу диапазона: '))
max_border = int(input('Ввелите верхнюю границу диапазона: '))

def Range_min_max(min_border, max_border):
    dict_1 ={}
    for i in range(min_border, max_border + 1):
        dict_1[i] = 0
    return dict_1

def Index_list(list_1, dict_1):
    list_2 =[]
    for i in range(len(list_1)):
        if list_1[i] in dict_1:
            list_2.append(i)
    return list_2

print(Index_list(list_1, Range_min_max(min_border, max_border)))

        