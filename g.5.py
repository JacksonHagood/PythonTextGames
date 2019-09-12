# game 5

# full text scramble
# all solutions are python related

import random

# set possible solutions, the solution, and the scrambled answer
words = ['python', 'programming', 'variable', 'integer', 'float', 'complex', 'string', 'boolean',
         'list', 'set', 'tuple', 'dictionary', 'immutable', 'index', 'condition', 'iterator',
         'import', 'math', 'random', 'function', 'define', 'return', 'casting', 'print', 'input',
         'append', 'commenting', 'operators', 'and', 'or', 'not', 'is', 'in', 'jackson', 'hagood']

word = words[random.randint(0, len(words) - 1)]

solution = list(word)
random.shuffle(solution)

lives = 10


def draw():
    # draws the scrambled answer
    print(lives, 'lives | ', end='')
    for char in solution:
        print(char, end='')
    print('')


# introduction
print('')
print('Welcome to Scramble!')
print('You must guess the word')
print('You have 10 lives')
print('')

while True:
    # runs through the game
    draw()
    guess = input('Your Guess: ')
    lives -= 1

    if guess == word:
        print('\nYou Win! :)')
        file = open('Board.txt', 'a')
        file.write(input('Enter Your Name: ') + ' Won in Scramble\n')
        file.close()
        break
    elif guess == '' or lives == 0:
        print('\nGame Over! :(')
        print('The answer was', '"' + word + '"')
        break

print('Thanks for playing!')
