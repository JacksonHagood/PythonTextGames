# game 4

# full text hangman
# all solutions are python related

import random

# set possible solutions, the solution, and the working answer
words = ['python', 'programming', 'variable', 'data type', 'integer', 'float', 'complex', 'string', 'boolean',
         'list', 'set', 'tuple', 'dictionary', 'immutable', 'index', 'condition', 'if statement', 'while loop',
         'for loop', 'iterator', 'import', 'math', 'random', 'function', 'define', 'return', 'casting',
         'augmented assignment', 'print', 'input', 'append', 'commenting', 'data science', 'operators', 'and',
         'or', 'not', 'is', 'is not', 'in', 'not in', 'jackson', 'hagood', 'python camp']

word = words[random.randint(0, len(words) - 1)]
solution = []
answer = []

lives = 10
index = 0

for char in word:
    solution.append(word[index])
    index += 1

for char in word:
    if char == ' ':
        answer.append(' ')
    else:
        answer.append('?')


def draw():
    # draws the working answer
    print(lives, 'lives | ', end='')
    for c in answer:
        print(c, end='')
    print('')


def check(guess):
    # checks a given character
    che = False
    i = 0
    if guess in answer:
        return False
    for c in word:
        if c == guess:
            answer[i] = guess
            che = True
        i += 1
    return che


# introduction
print('')
print('Welcome to Hangman!')
print('You must guess all letters')
print('You have 10 lives')
print('')

while True:
    # runs through the game
    draw()

    if not check(input('Your Guess: ')):
        lives -= 1

    if lives == 0:
        print('\nGame Over! :(')
        break

    if answer == solution:
        print('\nYou Win! :)')
        break

print('The answer was', '"' + word + '"')
print('Thanks for playing!')
