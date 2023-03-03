# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

digit = (input("Введите вещественное число через запятую: "))
index = list(digit)
index.remove(',')
result = [int(i) for i in index]
sum = 0
for e in result:
    sum += e
print(sum)