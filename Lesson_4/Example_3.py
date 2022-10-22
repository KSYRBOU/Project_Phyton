# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

from ast import NotIn


digit = int(input("Задайте размер списка: "))
s = []

def insert_list(l):
    for i in range(digit):
       value = int(input('Ввведите элемент списка:'))
       l.append(value)
    return l

def ind_elements(l1):
    temp = []
    for i in l1:
     if l1.count(i) == 1:
       temp.append(i)
    return temp

new_list = insert_list(s)
print(new_list)
ind_list = ind_elements(new_list)
print(ind_list)
