# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

l = [1, 5, 7, 14, 67, 32, 45, 78]
sum = 0
count = 0
while count < len(l):
    sum = sum + l[count]
    count = count + 2
print(sum)
