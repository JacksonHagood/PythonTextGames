# game 7

# full text matching game
# multiple size possible

import random
import math

# symbols contains all possible icons
symbols = ['X', 'X', 'O', 'O', 'J', 'J', '=', '=', '+', '+', '#', '#', '@', '@', '*', '*', '!', '!',
           '~', '~', '^', '^', '&', '&', '$', '$', '%', '%', '|', '|', '.', '.', '/', '/', '"', '"']

# index1 and index2 serve multiple purposes and correct holds number of matches
index1 = 0
index2 = 0
correct = 0

# solution contains icons and board is the blank cover
solution = []
board = []

# size controls the size of the board, can be set to 4, 16, or 36
size = 4

while True:
    # sets solution according to size
    index = random.randint(0, size - 1)
    if symbols[index] != ' ':
        solution.append(symbols[index])
        symbols[index] = ' '
    if len(solution) == size:
        break

for i in range(size):
    # sets board according to size
    board.append('-')


def draw(i1, i2):
    # draws board according to given indexes
    pos = 0
    if i1 >= 0:
        board[i1] = solution[i1]
    if i2 >= 0:
        board[i2] = solution[i2]
    for i in range(int(math.sqrt(size))):
        for j in range(int(math.sqrt(size))):
            print('[', board[pos], ']', sep='', end='')
            pos += 1
        print('')
    board[i1] = '-'
    board[i2] = '-'


# introduction
print('')
print('Welcome to Matching!')
print('You must guess all', int(size / 2), 'pairs')
print('The board is numbered as:')
print('')
index1 = 0
for index2 in range(int(math.sqrt(size))):
    for correct in range(int(math.sqrt(size))):
        if index1 < 10:
            index1 = '0' + str(index1)
        print('[', index1, ']', sep='', end='')
        index1 = int(index1)
        index1 += 1
    print('')
correct = 0

while True:
    # runs through the game
    print('-' * 100)
    draw(-1, -1)
    index1 = int(input('Card 1: '))
    draw(index1, -1)
    index2 = int(input('Card 2: '))
    draw(index1, index2)
    if solution[index1] == solution[index2]:
        board[index1] = ' '
        board[index2] = ' '
        correct += 1
        print('Match!')
    else:
        print('No Match!')
    if correct == size / 2:
        print('\nYou Win! :)')
        break

print('Thanks for playing!')
