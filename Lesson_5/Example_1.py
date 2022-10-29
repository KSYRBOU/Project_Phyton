# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст для обработки: ")

def del_words(s):
    s = list(filter(lambda x: 'абв' not in x, s.split()))
    return " ".join(s)

print(del_words(text))