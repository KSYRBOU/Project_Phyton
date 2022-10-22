# Вычислить число Пи c заданной точностью d

digit = float(input("Введите необходимую точность числа Пи: "))


def est_pi(acc):
    sum = 0
    d = 1
    sign = 1
    while True:
        a = 4/d
        sum = sum+sign*a
        if a < acc:
            return sum
        sign = -sign
        d = d+2


print(est_pi(digit))
