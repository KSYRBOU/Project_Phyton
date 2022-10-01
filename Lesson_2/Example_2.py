# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

digit = int (input("Введите целое число: "))
value = 1
for i in range(1,digit + 1):
    value = value * i
    print(value)