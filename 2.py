# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint


def firstTurn():
    return int(randint(0, 1))


def swapTurn(player):
    if player == name2:
        return name1
    else:
        return name2


def win(rest):
    win = True
    if rest > take:
        win = False
    if win:
        return win


candies = int(input('How many candies do we have? '))
take = int(input('Insert, how many MAX candies can player take: '))
name1 = input("Insert first player's name: ")
name2 = input("Insert second player's name: ")
players = {name1: 0, name2: 0}

perfectTurn = candies % (take + 1)

if firstTurn() == 0:
    player = name1
else:
    player = name2

while True:
    if player == 'bot':
        players[player] = int(randint(1, take))
        print(f'Player {player} takes {players[player]} candies')
    elif player == 'smartbot':
        players[player] = perfectTurn
        print(f'Player {player} takes {players[player]} candies')

    else:
        players[player] = int(input(f'Player {player} take candies: '))

    candies -= players[player]
    player = swapTurn(player)
    if win(candies):
        print(f'Player {player} wins!')
        break
