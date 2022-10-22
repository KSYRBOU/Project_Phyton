# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

digit = int(input("Введите число для нахождения простых множителей: "))


def mult_calc(N):
    count = 2
    s = []
    while count * count <= N:
        while N % count == 0:
            s.append(count)
            N = N/count
        count = count + 1
    if N > 1:
        s.append(N)
    return s


print(mult_calc(digit))
