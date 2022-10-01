# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

digit = (input("Введите вещественное число через запятую: "))
split = digit.split(',')
left_array = int(split[0])
right_array = int(split[1])
sum_r=0
sum_l=0
total = 0
while (left_array != 0): 
    sum_l = sum_l + (left_array % 10)
    left_array = left_array // 10
while (right_array != 0): 
    sum_r = sum_r + (right_array % 10)
    right_array = right_array // 10
total = sum_l + sum_r
print(total)