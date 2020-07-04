# game 11

# full text connect four
# ai is completely random

import random

# generate the blank board
board = []
for row in range(6):
    board.append([])
    for col in range(7):
        board[row].append(' ')


def draw():
    # draws the current board according to filled slots
    print('\n+-0-+-1-+-2-+-3-+-4-+-5-+-6-+')
    for i in range(6):
        for j in range(7):
            print('| ' + board[i][j] + ' ', end='')
        print('|')
        print('+-' + '--+-' * 6 + '--+')


def player():
    # runs the players turn
    slot = int(input('\nYour move: '))
    if board[0][slot] == ' ':
        for i in range(6):
            if board[i][slot] != ' ':
                board[i - 1][slot] = 'X'
                break
        else:
            board[5][slot] = 'X'
    else:
        print('That space is filled!')


def cpu():
    # runs the cpu turn
    while True:
        slot = random.randint(0, 6)
        if board[0][slot] == ' ':
            for i in range(6):
                if board[i][slot] != ' ':
                    board[i - 1][slot] = 'O'
                    break
            else:
                board[5][slot] = 'O'
            break


def full():
    # checks if board is full
    count = 0
    for i in range(6):
        for j in range(7):
            if board[i][j] != ' ':
                count += 1
    return count == 42


def win(s):
    # checks to see if given symbol has won

    # checks across
    for i in range(6):
        for j in range(4):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == s:
                board[i][j] = board[i][j + 1] = board[i][j + 2] = board[i][j + 3] = '#'
                return True

    # checks down
    for i in range(7):
        for j in range(3):
            if board[j][i] == board[j + 1][i] == board[j + 2][i] == board[j + 3][i] == s:
                board[j][i] = board[j + 1][i] = board[j + 2][i] = board[j + 3][i] = '#'
                return True

    # checks diagonal right
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == s:
                board[i][j] = board[i + 1][j + 1] = board[i + 2][j + 2] = board[i + 3][j + 3] = '#'
                return True

    # checks diagonal left
    for i in range(3, 7):
        for j in range(3):
            if board[j][i] == board[j + 1][i - 1] == board[j + 2][i - 2] == board[j + 3][i - 3] == s:
                board[j][i] = board[j + 1][i - 1] = board[j + 2][i - 2] = board[j + 3][i - 3] = '#'
                return True

    return False


# introduction
print('\nWelcome to Connect Four!'
      '\nYou are X, the CPU is O'
      '\nSlots are numbered 0 - 6'
      '\nGet 4 in any direction')

while True:
    # runs through the game

    draw()
    player()

    if win('X'):
        draw()
        print('\nYou Win! :)')
        file = open('Board.txt', 'a')
        file.write(input('Enter Your Name: ') + ' Won in Connect Four\n')
        file.close()
        break
    elif full():
        print('\nTie')
        break

    cpu()

    if win('O'):
        draw()
        print('\nGame Over! :(')
        break
    elif full():
        print('\nTie')
        break

print('Thanks for playing!')
