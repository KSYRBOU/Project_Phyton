# Задайте список из n чисел последовательности (1+1/n)*n и выведите на экран их сумму

digit = int (input("Введите целое число: "))
value = 0
s = []
e= 0
total = 0

for i in range(1,digit + 1):
    value = value + ((i+1)/i)**i
    s.append(value)

for e in range(len(s)):
    total = total + round(s[e])
        
print("Сумма чисел последовательности при n", digit, "будет =", total)