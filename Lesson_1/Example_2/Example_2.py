#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
#в которой находится эта точка (или на какой оси она находится).

x = int (input("Введите X координату точки не равную нулю: "))
y = int (input("Введите Y координату точки не равную нулю: "))

if x > 0 and y > 0:
    print('Точка находится в I четверти!')
if x < 0 and y < 0:
    print('Точка находится в IV четверти!')
if x < 0 and y > 0:
    print('Точка находится в II четверти!')
if x > 0 and y < 0:
    print('Точка находится в III четверти!')