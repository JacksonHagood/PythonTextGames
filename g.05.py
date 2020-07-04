# game 5

# full text scramble
# all solutions are python related

from random import randint, shuffle

# set the number of lives and possible solutions
lives = 5
words = ['python', 'programming', 'variable', 'integer', 'float', 'complex', 'string', 'boolean',
         'list', 'set', 'tuple', 'dictionary', 'immutable', 'index', 'condition', 'iterator',
         'import', 'math', 'random', 'function', 'define', 'return', 'casting', 'print', 'input',
         'append', 'commenting', 'operators', 'and', 'or', 'not', 'is', 'in', 'jackson', 'hagood']

# generate the word and translate it into a list that is randomized
word = words[randint(0, len(words) - 1)]
answer = list(word)
shuffle(answer)


def draw():
    """draws the scrambled word"""

    print('\n' + str(lives), 'lives | ', end='')
    for c in answer:
        print(c, end='')
    print('')


# introduction
print('\nWelcome to Scramble!'
      '\nYou must guess the word'
      '\nYou have 5 lives')

# run through the game
while True:
    # draw board and run player turn
    draw()
    guess = input('Your Guess: ')
    lives -= 1

    # check for a loss or win and output accordingly
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

# closing statement
print('Thanks for playing!')
