# Реализуйте алгоритм перемешивания списка

import random
digit = int (input("Введите размер списка: "))
value = 0
s = []

def shuffle_list (l):
    temp = l[0]
    temp1 = l[-1]
    for i in range(len(l)-1):
        l.insert(i,l[i+1])
        l.remove(l[i+1])
    l.remove(temp1)
    l.append(temp)
    return l 
    
def insert_list (l1):
    for e in range(0,digit):
        value = random.randint(1,100)
        l1.append(value)
    return l1

new_list = insert_list(s)
print(new_list)
shuffled = shuffle_list(new_list)
print(shuffled)

        
