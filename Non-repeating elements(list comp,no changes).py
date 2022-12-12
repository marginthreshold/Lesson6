# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

import os

os.system('cls||clear')

user_lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]


def non_repeating_elements_in_list(lst):
    non_repeat = [i for i in lst if lst.count(i) == 1]
    print(non_repeat)


non_repeating_elements_in_list(user_lst)