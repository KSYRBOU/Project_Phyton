# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

first_element = int(input("Введите первый элемент прогрессии: "))
diff_elements = int(input("Введите разнось элементов прогрессии: "))
amount_elements = int(input("Введите количество элементов: "))

for i in range(amount_elements):
    print(first_element + i * diff_elements)