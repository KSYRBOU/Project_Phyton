# Напишите функцию, которая принимает число в качестве ввода, возводит
# его в квадрат и возвращает.

try:
    digit = float(input("Задайте число: "))
except(ValueError):
    print("Ошибка ввода!")

def sqrt_func(num):
    return num*num

print(sqrt_func(digit))
