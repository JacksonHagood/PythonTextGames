# game 2

# full text adventure game
# section 1 consists of guessing a random number
# section 2 consists of answering a multiple choice question
# section 3 consists of naming as many items as possible

import random
import sys

# section 1

print('-' * 100)
# separates sections

print('You approach the mysterious gates of PyLand')
print('A lock running 0 to 100 holds the gates shut')
print('The lock must be opened within 10 guesses')

solution = random.randint(0, 99)
# assign the solution randomly each time
count = 0
# count controls the number of guesses
answer = 0

while count < 10:
    # feedback is given in relation to the solution
    answer = int(input('Your Guess: '))
    if answer == solution:
        break
    elif answer > 100 or answer < 0:
        break
    elif answer > solution:
        print('Your guess was too high')
    else:
        print('Your guess was too low')
    count += 1

if answer == solution:
    print('The gates open, and you walk into PyLand')
else:
    sys.exit('You have failed, and the gates remain shut')
    # sys.exit will quit the game

# section 2

print('-' * 100)

print('As you enter PyLand a man appears in front of you')
print('The man begins to speak, and asks for your name')
name = input('Your Name: ')

choices = ['A - Lists', 'B - Sets', 'C - Tuples', 'D - Dictionaries']
# answer choices are stored in a list

print('Hello', name + ', to move on you must answer this question:')
print('Of the following, which is immutable?')
for choice in choices:
    # list is iterated through
    print(choice)

answer = input('Your Answer: ').upper()
# .upper() eliminates the ambiguity in capitalization

if answer == 'C':
    print('Correct! You have learned well and may go on')
else:
    sys.exit('You have failed, and the man exiles you')

# section 3

print('-' * 100)

answers = []
# answers stored as a list
count = 0

print('Finally a voice calls to you', name)
print('The voice asks you to name as many data types as you can')

while True:
    answer = input('Data Type: ').upper()
    if answer == '':
        break
        # pressing enter exits the input
    answers.append(answer)

for guess in answers:
    if guess in 'INTEGER FLOAT COMPLEX STRING BOOLEAN LIST SET TUPLE DICTIONARY':
        count += 1

# depending on the amount guessed, an ability will be printed
if count < 1:
    sys.exit('You have failed, and the voice exiles you')
elif count < 3:
    print('You are beginner in Python')
elif count < 5:
    print('You are intermediate in Python')
elif count < 7:
    print('You are advanced in Python')
elif count < 9:
    print('You are professional in Python')
else:
    print('You are perfect in Python!')

# end

print('-' * 100)

file = open('Board.txt', 'a')
file.write(input('Enter Your Name: ') + ' Played an Adventure Game\n')
file.close()
print('Thanks for Playing!')
