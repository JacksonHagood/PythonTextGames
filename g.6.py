# game 6

# full text word search
# all solutions are python related

import random

# set possible solutions and what takes up the board
# possible solutions must be under 10 characters
words = ['python', 'float', 'string', 'list', 'set', 'tuple', 'index', 'import',
         'math', 'random', 'define', 'return', 'print', 'input', 'append', 'hagood']

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']

# board holds word search, taken holds values for where words are located
board = []
taken = []

# number holds how many solutions there are, solutions holds the working solutions, and guesses holds working guesses
number = 0
solutions = []
guesses = []

# correct holds correct number of guesses and length holds the size of the board
correct = 0
length = 9

# randomizes the board
for i in range(length):
    board.append([])
    for j in range(length):
        board[i].append(letters[random.randint(0, 25)])

# clears taken
for i in range(length):
    taken.append([])
    for j in range(length):
        taken[i].append(' ')


def checkrow(r):
    # checks if a given row is clear
    for i in range(length):
        if taken[r][i] == '-':
            return False
    return True


def checkcol(c):
    # checks if a given column is clear
    for i in range(length):
        if taken[i][c] == '-':
            return False
    return True


def draw():
    # draws the board
    print('')
    for i in range(length):
        for j in range(length):
            print(board[i][j], end =' ')
        print('')


# sets the solutions into the board
for i in range(25):
    ran = random.randint(0, len(words) - 1)
    word = words[ran].upper()
    words[ran] = '-'
    ran = random.randint(0, length - 1)
    j = 0
    # sets according to a row
    if random.randint(0, 1) == 0 and checkrow(ran) and not word == '-':
        j += random.randint(0, length - len(word) - 1)
        number += 1
        solutions.append(word)
        for char in word:
            board[ran][j] = char
            taken[ran][j] = '-'
            j += 1
    # sets according to a column
    elif checkcol(ran) and not word == '-':
        j += random.randint(0, length - len(word) - 1)
        number += 1
        solutions.append(word)
        for char in word:
            board[j][ran] = char
            taken[j][ran] = '-'
            j += 1

# introduction
print('')
print('Welcome to Word Search!')
print('You must find all words')
print('There are', number, 'solutions')

while True:
    # runs through the game
    draw()
    guess = input('Your Guess: ').upper()
    if guess in guesses:
        print('You have already guessed that')
    elif guess in solutions:
        print('Correct!')
        correct += 1
    else:
        print(guess, 'is not a solution')
    if correct == number:
        print('\nYou Win! :)')
        break
    guesses.append(guess)

print('The answers were: ', end ='')
for i in range(len(solutions) - 1):
    print('"' + solutions[i].lower() + '"', end=', ')
print('and', '"' + solutions[len(solutions) - 1].lower() + '"')
print('Thanks for playing!')
