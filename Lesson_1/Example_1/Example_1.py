#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
a = int (input("Введите число, обозначающее день недели = "))
index = a - 1
range = range(0,4)
count_days = list(range)
if index in count_days:
    print(week_days[index],'День не выходной!')
else:
    print(week_days[index],'День выходной!')