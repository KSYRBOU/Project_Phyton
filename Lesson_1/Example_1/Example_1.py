#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

week_days = [0,'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
index = 0
while index > 7 or index < 1:
    index = int (input("Введите число, обозначающее день недели = "))
if index in week_days[1:5]:
    print(week_days[index],'День не выходной!')
else:
    print(week_days[index],'День выходной!')
