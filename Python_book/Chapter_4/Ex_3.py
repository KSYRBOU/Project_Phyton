# Напишите функцию, которая принимает три обязательных и два необязательных параметра

def func_1(a, b, c, d = 2, e = 4):
    return a+b+c+d+e
print(func_1(2,3,5,8,9))