# Создайте программу для игры в "Крестики-нолики".


from random import randint


def emptyLine(lst):
    flag = True
    for i in lst:
        if '-' in i:
            flag = False
    return flag


def turn(lst, row, col, player):
    lst[row][col] = player


def anyWin(lst, player):
    win = None
    n = len(lst)

    # Проверка горизонталей
    for i in range(n):
        win = True
        for j in range(n):
            if lst[i][j] != player:
                win = False
                break
        if win:
            return win
    # Проверка вертикалей
    for i in range(n):
        win = True
        for j in range(n):
            if lst[j][i] != player:
                win = False
                break
        if win:
            return win
    # Проверка диагоналей
    win = True
    for i in range(n):
        if lst[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if lst[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False

    for row in lst:
        for i in row:
            if i == '-':
                return False
    return True


def swapTurn(player):
    if player == '0':
        return 'X'
    else:
        return '0'


def showBoard(lst):
    for i in lst:
        print(*i)


def firstTurn():
    return int(randint(0, 1))


n = int(input('Insert lines quantity: '))
board = [['-' for j in range(n)] for i in range(n)]

player = 'X' if firstTurn() == 1 else '0'

while True:
    print(f'Player {player} turn')
    showBoard(board)
    row, col = list(
        map(int, input('Insert row and column numbers to sign: ').split()))
    print()
    turn(board, row-1, col-1, player)
    if anyWin(board, player):
        print(f'Player {player} wins!')
        break
    if emptyLine(board):
        print('DRAW!')
        break
    player = swapTurn(player)

    print()
    showBoard(board)
