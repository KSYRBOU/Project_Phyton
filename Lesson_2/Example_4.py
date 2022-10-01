# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

digit = int (input("Введите целое число: "))
s = []
temp = 0
for i in range(digit, -digit + 1):
    s.append(-i)
f = open('lesson_2/file.txt')
for line in f:
    temp = int(line)
    print(s[temp])