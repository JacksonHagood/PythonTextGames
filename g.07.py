# game 7

# full text matching game
# multiple size possible

from random import randint
import math

# symbols contains all possible icons
symbols = ['X', 'X', 'O', 'O', 'J', 'J', '=', '=', '+', '+', '#', '#', '@', '@', '*', '*', '!', '!',
           '~', '~', '^', '^', '&', '&', '$', '$', '%', '%', '|', '|', '.', '.', '/', '/', '"', '"']

# initialize indexes, solutions, the board, and the size (size can be 4, 16, or 36)
index1, index2, correct, solution, board, size = 0, 0, 0, [], [], 16

# set solution according to size
while True:
    index = randint(0, size - 1)
    if symbols[index] != ' ':
        solution.append(symbols[index])
        symbols[index] = ' '
        board.append('-')
    if len(solution) == size:
        break


def draw(i1, i2):
    """draws board according to given indexes"""

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
print('\nWelcome to Matching!'
      '\nYou must guess all', int(size / 2), 'pairs'
      '\nThe board is numbered as:\n')
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

# run through the game
while True:
    # draw the board and run the player turn
    print('\n')
    draw(-1, -1)
    index1 = int(input('Card 1: '))
    draw(index1, -1)
    index2 = int(input('Card 2: '))
    draw(index1, index2)

    # check for solutions and output accordingly
    if solution[index1] == solution[index2]:
        board[index1] = ' '
        board[index2] = ' '
        correct += 1
        print('Match!')
    else:
        print('No Match!')

    # check for a win and output accordingly
    if correct == size / 2:
        print('\nYou Win! :)')
        file = open('Board.txt', 'a')
        file.write(input('Enter Your Name: ') + ' Won in Matching\n')
        file.close()
        break

# closing statement
print('Thanks for playing!')
