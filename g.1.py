# game 1

# full text tic tac toe
# ai is completely random

import random

filled = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def draw(board):
    # draws the current board according to filled slots
    print('')
    print('-' * 15)
    print('|    ' + board[0] + '|' + board[1] + '|' + board[2] + '    |')
    print('|    ' + '-' * 5 + '    |')
    print('|    ' + board[3] + '|' + board[4] + '|' + board[5] + '    |')
    print('|    ' + '-' * 5 + '    |')
    print('|    ' + board[6] + '|' + board[7] + '|' + board[8] + '    |')
    print('-' * 15)
    print('')


def check(board, slot):
    # checks if slot is blank
    return board[slot] == ' '


def player():
    # runs the players turn
    slot = int(input('Your move: '))
    if check(filled, slot):
        filled[slot] = 'X'
    else:
        print('That space is filled!')


def cpu():
    # runs the cpu turn
    while True:
        slot = random.randint(0, 8)
        if check(filled, slot):
            filled[slot] = 'O'
            break


def full(board):
    # checks if board is full
    count = 0
    for slot in board:
        if slot != ' ':
            count += 1
    return count == 9


def win(b, s):
    # checks to see if given symbol has won
    return ((b[0] == s and b[1] == s and b[2] == s) or
            (b[3] == s and b[4] == s and b[5] == s) or
            (b[6] == s and b[7] == s and b[8] == s) or
            (b[0] == s and b[3] == s and b[6] == s) or
            (b[1] == s and b[4] == s and b[7] == s) or
            (b[2] == s and b[5] == s and b[8] == s) or
            (b[0] == s and b[4] == s and b[8] == s) or
            (b[6] == s and b[4] == s and b[2] == s))


# introduction
print('')
print('Welcome to Tic Tac Toe!')
print('You are X, the CPU is O')
print('The board is numbered as:')
print('')
print('-' * 15)
print('|    0|1|2    |')
print('|    ' + '-' * 5 + '    |')
print('|    3|4|5    |')
print('|    ' + '-' * 5 + '    |')
print('|    6|7|8    |')
print('-' * 15)
print('')

while True:
    # runs through the game
    player()
    if win(filled, 'X'):
        draw(filled)
        print('You Win! :)')
        break
    elif full(filled):
        draw(filled)
        print('Tie')
        break

    cpu()
    draw(filled)

    if win(filled, 'O'):
        print('Game Over! :(')
        break
    elif full(filled):
        print('Tie')
        break

print('Thanks for playing!')
