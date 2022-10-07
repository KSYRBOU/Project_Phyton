# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

digit = int(input("Введите число для преобразования: "))


def dec_to_bin(i):
    s = []
    while i != 0:
        s.append(i % 2)
        i = i // 2
    s.reverse()
    for i in range(len(s)):
        print(s[i], end="")
    print(' - Двоичное число из ', digit)


result = dec_to_bin(digit)
