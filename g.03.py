# game 3

# full text adventure game
# section 1 consists of guessing a random number
# section 2 consists of answering a multiple choice question
# section 3 consists of naming as many items as possible

from random import randint

while True:
    # section 1
    print('\nYou approach the mysterious gates of PyLand'
          '\nA lock running 0 to 100 holds the gates shut'
          '\nThe lock must be opened within 10 guesses')

    # assign a random solution and store the guess and number of guesses
    solution, count, answer = randint(0, 99), 0, 0

    # go through input and give feedback accordingly until a condition is met
    while count < 10:
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

    # output accordingly
    if answer == solution:
        print('The gates open, and you walk into PyLand')
    else:
        print('Game Over! :(')
        break

    # section 2
    print('\nAs you enter PyLand a man appears in front of you'
          '\nThe man begins to speak, and asks for your name')

    # take in user name
    name = input('Your Name: ')

    # ask question and output choices
    choices = ['A - Lists', 'B - Sets', 'C - Tuples', 'D - Dictionaries']
    print('Hello', name + ', to move on you must answer this question:'
          '\nOf the following, which is immutable?')
    for choice in choices:
        print(choice)

    # take in input and check answer with corresponding output
    answer = input('Your Answer: ').upper()
    if answer == 'C':
        print('Correct! You have learned well and may go on')
    else:
        print('\nGame Over! :(')
        break

    # section 3
    print('\nFinally a voice calls to you', name +
          '\nThe voice asks you to name as many data types as you can')

    # store user answers and the number of them
    answers, count = [], 0

    # accept input repeatedly
    while True:
        answer = input('Data Type: ').upper()
        if answer == '':
            break
        answers.append(answer)

    # check input and output accordingly
    for guess in answers:
        if guess in 'INTEGER FLOAT COMPLEX STRING BOOLEAN LIST SET TUPLE DICTIONARY':
            count += 1
    if count < 1:
        print('\nGame Over! :(')
        break
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

    # section 4
    print('\nYou Win! :)')
    file = open('Board.txt', 'a')
    file.write(name + ' Played an Adventure Game\n')
    file.close()
    break

# closing statement
print('Thanks for Playing!')
