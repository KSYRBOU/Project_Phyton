# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
digit = int(input("Введите размер списка: "))
s = []
rev_list = []


def insert_list(l1):
    value = 0
    for e in range(0, digit):
        value = random.randint(1, 100)
        l1.append(value)
    return l1


new_list = insert_list(s)
print(new_list)
rev_list = new_list.copy()
rev_list.reverse()
print(rev_list)

if digit % 2 == 0:
    for i in range(digit // 2):
        print(new_list[i]*rev_list[i])
else:
    for i in range(round(digit // 2)+1):
        print(new_list[i]*rev_list[i])
