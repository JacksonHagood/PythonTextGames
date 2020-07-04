# game 10

# full text Yahtzee!
# 1 player version

from random import randint


def instructions():
    """prints the instructions of the game to the user"""

    print('\n   ' + '-' * 11 + 'Yahtzee Instructions' + '-' * 11 +
          '\n   ' + 'There are five dice that will be rolled'
          '\n   ' + '(numbered 1-5 left to right). Each turn the'
          '\n   ' + 'dice will be rolled, then the user can'
          '\n   ' + 'select certain dice to be rolled again.'
          '\n   ' + 'After 3 total rolls the turn is over, and'
          '\n   ' + 'the user chooses to score them out of 7'
          '\n   ' + 'categories:'
          '\n   ' + '3 of a kind        (three)     sum of dice.'
          '\n   ' + '4 of a kind        (four)      sum of dice.'
          '\n   ' + '2 and 3 of a kind  (full)      25.'
          '\n   ' + '4 sequential       (small)     30.'
          '\n   ' + '5 sequential       (large)     40.'
          '\n   ' + '5 of a kind        (yahtzee)   50.'
          '\n   ' + 'Any                (chance)    sum of dice.'
          '\n   ' + 'There are 13 total turns, and no category'
          '\n   ' + 'can be used twice. Additionally, there is'
          '\n   ' + 'an upper score that is the sum of the dice,'
          '\n   ' + 'which is counted every turn. Call dice in'
          '\n   ' + 'the format 1-5 and the way to be graded'
          '\n   ' + 'the list above.'
          '\n   ' + '-' * 11 + 'Yahtzee Instructions' + '-' * 11 + '\n')


def turn():
    """Goes through a single turn of the game."""

    # initialize variables
    dice, re = [], []

    # iterate through 3 total dice rolls
    for i in range(3):
        # on the first roll, roll all dice
        if i == 0:
            dice += roll(5)
        # on subsequent rolls, allow specific rolling of dice
        else:
            # reset variables
            die, re = 'temp', []

            # output dice
            print('   Dice:', dice)

            # get dice to roll again from input
            while die != 0:
                # if the user inputs dice 0, stop
                die = input('   Enter a dice number to roll again (0 to stop): ')

                if die in '0123456789':
                    die = int(die)

                    # add indexes of dice to a list
                    if 0 < die <= 5:
                        re.append(die - 1)
            print('')

            # roll dice again
            for j in re:
                dice[j] = roll(1)[0]

    # output and return dice
    print('   Dice:', dice)
    return dice


def roll(rolls):
    """Rolls the amount of dice passed through."""

    # initialize dice
    dice = []

    # roll dice according to rolls
    for i in range(rolls):
        dice.append(randint(1, 6))

    # return dice
    return dice


def score(dice, method):
    """Returns the score of the passed dice using the passed method."""

    # initialize points
    points = 0

    # evaluate three of a kind
    if method == 'three':
        # if there exists three of a kind, add the dice summed
        for i in range(1, 7):
            if dice.count(i) >= 3:
                points += sum(dice)

    # evaluate four of a kind
    elif method == 'four':
        # if there exists four of a kind, add the dice summed
        for i in range(1, 7):
            if dice.count(i) >= 4:
                points += sum(dice)

    # evaluate a full house
    elif method == 'full':
        # if there exists both a two and three of a kind add 25
        a, b = False, False
        for i in range(1, 7):
            if dice.count(i) == 3:
                a = True
            if dice.count(i) == 2:
                b = True
        if a and b:
            points += 25

    # evaluate a small sequence
    elif method == 'small':
        # if there exists a sequence of 4 numbers add 30
        for i in range(1, 7):
            if dice.count(i) == 2:
                dice.remove(i)
        dice = ''.join(str(i) for i in sorted(dice))
        if '1234' in dice or '2345' in dice or '3456' in dice:
            points += 30

    # evaluate a large sequence
    elif method == 'large':
        # if there exists a sequence of 5 numbers add 40
        dice = ''.join(str(i) for i in sorted(dice))
        if '12345' in dice or '23456' in dice:
            points += 40

    # evaluate five of a kind
    elif method == 'yahtzee':
        # if there exists five of a kind, add 50
        for i in range(1, 7):
            if dice.count(i) == 5:
                points += 50

    # evaluate a chance
    elif method == 'chance':
        # add the dice summed
        points += sum(dice)

    # return points
    return points


# instructions
print('Welcome to Yahtzee!')
instructions()

# initialize variables
score1, score2, way, previous, q = 0, 0, '', [], False

# initialize repeat from input
repeat = input('Enter "y" to allow repeated scoring methods: ')
print('-' * 100)

# iterate through the thirteen turns
for t in range(13):
    # output the current turn
    print('TURN', t + 1)

    # allow the user to view one of several items
    option = input('   (i: instructions, q: quit, or s: score): ')

    # output the indicated item
    if option == 'q':
        # allow the user to quit the game
        q = True
        break
    elif option == 'i':
        # allow the user to view the instructions
        instructions()
    elif option == 's':
        # allow the user to view the current score
        print('   Current score:', score1 + score2)
    # run through a turn, set the dice to final
    final = turn()

    # increment score 1 by the dice
    score1 += sum(final)

    # ask the user for a way to score
    way = input('   Enter the way to score (n for none): ')

    # ensure the method has not been used
    if way not in previous or repeat == 'y':
        # add the method to the list of methods used
        previous.append(way)

        # increment score 2 by the dice scored with the method
        score2 += score(final, way)
    print('-' * 100)

# ensure the user has not quit
if not q:
    # add an additional 35 points if score 1 exceeded 63
    if score1 >= 63:
        score1 += 35

    # output final scores
    print('DONE!')
    print('   Upper score:', score1)
    print('   Lower score:', score2)
    print('   Final score:', score1 + score2)

    # open file for output
    File = open('Board.txt', 'a')

    # allow the user to input their name
    name = input('   Enter a name: ')

    # write the user's name and score to the file
    File.write(name + ' Played Yahtzee! with a final score of ' + str(score1 + score2) + '\n')

    # close the file
    File.close()

# output a final message to the user
print('-' * 100)
print('Thanks for playing!')
