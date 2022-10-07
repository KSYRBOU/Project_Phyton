# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

digit = int(input("Введите размер списка: "))
s = [0,1]

def insert_list(l):
    value = 0
    for i in range(2, digit):
        value = l[i+2] - l[i+1]
        l.append(value)
    #for e in range(2, digit):
    #   value = l[e-2] + l[e-1]
    #    l.append(value)
    return l

new_list = insert_list(s)
print(new_list)
