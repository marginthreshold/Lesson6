# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
os.system('cls||clear')

lst = [2, 3, 4, 9, 3 ]


def sum_of_odd_elements(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum


def sum_of_odd_elements_new(list):
    sum = 0
    for count, el in enumerate(list):
        if count % 2 != 0:
            sum+=el
    return sum

print(sum_of_odd_elements(lst))
print(sum_of_odd_elements_new(lst))

