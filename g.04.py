# game 4

# full text hangman
# all solutions are python related

from random import randint

# set the number of lives and possible solutions
lives = 10
words = ['python', 'programming', 'variable', 'data type', 'integer', 'float', 'complex', 'string', 'boolean',
         'list', 'set', 'tuple', 'dictionary', 'immutable', 'index', 'condition', 'if statement', 'while loop',
         'for loop', 'iterator', 'import', 'math', 'random', 'function', 'define', 'return', 'casting',
         'augmented assignment', 'print', 'input', 'append', 'commenting', 'data science', 'operators', 'and',
         'or', 'not', 'is', 'is not', 'in', 'not in', 'jackson', 'hagood', 'python camp']

# generate the word and translate it into lists
word, solution, answer = words[randint(0, len(words) - 1)], [], []
for char in word:
    solution.append(char)
    if char == ' ':
        answer.append(' ')
    else:
        answer.append('?')


def draw():
    """draws the working answer"""

    print('\n' + str(lives), 'lives | ', end='')
    for c in answer:
        print(c, end='')
    print('')


def check(guess):
    """checks a given character"""

    correct = False
    for i in range(len(word)):
        if word[i] == guess:
            answer[i] = guess
            correct = True
    return correct


# introduction
print('\nWelcome to Hangman!'
      '\nYou must guess all letters'
      '\nYou have 10 lives')

# run through the game
while True:
    # draw board and run player turn
    draw()
    if not check(input('Your Guess: ').lower()):
        lives -= 1

    # check for a loss or win and output accordingly
    if lives == 0:
        print('\nGame Over! :(')
        print('The answer was', '"' + word + '"')
        break
    if answer == solution:
        print('\nYou Win! :)')
        file = open('Board.txt', 'a')
        file.write(input('Enter Your Name: ') + ' Won in Hangman\n')
        file.close()
        break

# closing statement
print('Thanks for playing!')
