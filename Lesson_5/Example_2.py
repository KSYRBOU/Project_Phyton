# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

messages = ['Возьмите конфеты', 'Ваш ход']

def play_game(n, m, players, messages):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Можно взять не более {m} конфет{letter}, всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'У Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Не осталось попыток!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Больше нет конфет!')
        count +=1
    return players[not count%2]

player1 = input('Игрок 1, представьтесь, пожалуйста!\n')
player2 = input('Игрок 2, представьтесь, пожалуйста!\n')
players = [player1, player2]

n = int(input('Сколько конфет всего?\n '))
m = int(input('Сколько конфет за ход?\n '))

winer = play_game(n, m, players, messages)
if not winer:
    print('Нет победителя!')
else: print(f'Победитель {winer}!')