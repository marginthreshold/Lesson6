# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.
from itertools import zip_longest
import os

os.system('cls||clear')


polynomial_first = open("polynomial_1.txt", "r")
line_one = polynomial_first.readline()
print(line_one)
polynomial_first.close

polynomial_second = open("polynomial_2.txt", "r")
line_two = polynomial_second.readline()
print(line_two)
polynomial_second.close


line_one = line_one.replace("*x^", " ")
line_one = line_one.replace("+ ", "")
line_one = line_one.replace("- ", "-")
line_one = line_one.replace("*x", " 1")


line_two = line_two.replace("*x^", " ")
line_two = line_two.replace("+ ", "")
line_two = line_two.replace("- ", "-")
line_two = line_two.replace("*x", " 1")


lst_one = [int(i) for i in line_one.split(" ")]
lst_two = [int(i) for i in line_two.split(" ")]


def add_degree(lst1, lst2):
    dict_lst = 0
    if lst1[1] > lst2[1]:
        diff_lst = lst1[1]-lst2[1]
        for i in range(0, diff_lst*2-1, 2):
            lst2.insert(i, 0)
            lst2.insert(i+1, lst1[1]-i)
    elif lst1[1] < lst2[1]:
        diff_lst = lst2[1]-lst1[1]
        for i in range(0, diff_lst*2-1, 2):
            lst1.insert(i, 0)
            lst1.insert(i+1, lst2[1]-i)


def net_polynominal(lst):
    new_lst = []
    count = lst[1]
    i = 0
    while i < len(lst)-1:
        if lst[i+1] == count:
            new_lst.append(lst[i])
            count -= 1
            i += 2
        else:
            new_lst.append(0)
            count -= 1
    new_lst.append(lst[-1])
    return new_lst


def print_polynomial(lst):
    string_polynomial = "" if lst[0] == 0 else str(
        lst[0])+"*x^"+str(len(lst)-1)
    for i in range(1, len(lst)-2):
        string_polynomial = string_polynomial + \
            "" if lst[i] == 0 else string_polynomial + \
            " + "+str(lst[i])+"*x^"+str(len(lst)-i-1)
    string_polynomial_last = "" if lst[-2] == 0 else " + "+str(lst[-2])+"*x"
    lst_last = "" if lst[-1] == 0 else " + "+str(lst[-1])
    return string_polynomial+string_polynomial_last+lst_last


def sum_polinomial(lst1, lst2):
    new_lst = [i+j for i, j in zip_longest(lst1, lst2, fillvalue=0)]
    return new_lst


add_degree(lst_one, lst_two)

lst_polynomial_one = net_polynominal(lst_one)
print(lst_polynomial_one)

lst_polynomial_two = net_polynominal(lst_two)
print(lst_polynomial_two)

lst_sum_polynomial = print_polynomial(
    sum_polinomial(lst_polynomial_one, lst_polynomial_two))
print(lst_sum_polynomial)

polinomial_file = open("sum polynomial.txt", "w")
polinomial_file.writelines(lst_sum_polynomial)
polinomial_file.close
