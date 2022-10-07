# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов

from decimal import Decimal
digit = int(input("Введите размер списка: "))
s = []


def comparison(l):
    max = l[0]
    min = l[0]
    dif = 0
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
        if l[i] < min:
            min = l[i]
    dif = max - min
    print(dif)


def insert_list(l1):
    value = 0
    for e in range(0, digit):
        value = float(Decimal(e+10) / 100)
        l1.append(value)
    return l1


new_list = insert_list(s)
print(new_list)
comp_list = comparison(new_list)
