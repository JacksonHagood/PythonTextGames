# game 6

# full text word search
# all solutions are python related

from random import randint

# set possible solutions and the letters, solutions must be under 10 characters
words = ['python', 'variable', 'integer', 'float', 'complex', 'string', 'boolean', 'list', 'set',
         'tuple', 'index', 'iterator', 'import', 'math', 'random', 'function', 'define', 'return',
         'casting', 'print', 'input', 'append', 'and', 'or', 'not', 'is', 'in', 'jackson', 'hagood',
         'module']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']

# initialize variables for the board, solutions, filled spots, and the length
board, taken, number, solutions, guesses, correct, length = [], [], 0, [], [], 0, 9

# randomize the board and set taken
for m in range(length):
    board.append([])
    taken.append([])
    for n in range(length):
        board[m].append(letters[randint(0, 25)])
        taken[m].append(' ')



def checkrow(r):
    """checks if a given row is clear"""

    for i in range(length):
        if taken[r][i] == '-':
            return False
    return True


def checkcol(c):
    """checks if a given column is clear"""

    for i in range(length):
        if taken[i][c] == '-':
            return False
    return True


def draw():
    """draws the board"""

    print('')
    for i in range(length):
        for j in range(length):
            print(board[i][j], end=' ')
        print('')


# generate the board with solutions
for m in range(100):
    ran = randint(0, len(words) - 1)
    word = words[ran].upper()
    words[ran], ran, n = '-', randint(0, length - 1), 0

    # set potential solution into a row
    if randint(0, 1) == 0 and checkrow(ran) and not word == '-':
        n += randint(0, length - len(word) - 1)
        number += 1
        solutions.append(word)

        for char in word:
            board[ran][n] = char
            taken[ran][n] = '-'
            n += 1

    # set potential solution into a column
    elif checkcol(ran) and not word == '-':
        n += randint(0, length - len(word) - 1)
        number += 1
        solutions.append(word)

        for char in word:
            board[n][ran] = char
            taken[n][ran] = '-'
            n += 1

# introduction
print('\nWelcome to Word Search!'
      '\nYou must find all words'
      '\nThere are', number, 'solutions')

# run through the game
while True:
    # draw board and run player turn
    draw()
    guess = input('\nYour Guess: ').upper()
    if guess in guesses:
        print('"' + guess.lower() + '" has already been guessed')
    elif guess in solutions:
        print('Correct!')
        correct += 1
    else:
        print('"' + guess.lower() + '" is not a solution')

    # check for a win and output accordingly
    if correct == number:
        print('\nYou Win! :)')
        print('The answers were: ', end='')
        for i in range(len(solutions) - 1):
            print('"' + solutions[i].lower() + '"', end=', ')
        print('and', '"' + solutions[len(solutions) - 1].lower() + '"')

        file = open('Board.txt', 'a')
        file.write(input('Enter Your Name: ') + ' Won in Word Search\n')
        file.close()
        break

    guesses.append(guess)

# closing statement
print('Thanks for playing!')
