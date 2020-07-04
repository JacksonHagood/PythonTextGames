# game 10

# full text Yahtzee!
# 1 player version

# Imports.
from random import *

# Functions.


# Define instructions.
def instructions():
    """Prints the instructions of the game to the user."""

    # Page of instructions.
    print('')
    print('   ' + '-' * 11 + 'Yahtzee Instructions' + '-' * 11)
    print('   ' + 'There are five dice that will be rolled')
    print('   ' + '(numbered 1-5 left to right). Each turn the')
    print('   ' + 'dice will be rolled, then the user can')
    print('   ' + 'select certain dice to be rolled again.')
    print('   ' + 'After 3 total rolls the turn is over, and')
    print('   ' + 'the user chooses to score them out of 7')
    print('   ' + 'categories:')
    print('   ' + '3 of a kind        (three)     sum of dice.')
    print('   ' + '4 of a kind        (four)      sum of dice.')
    print('   ' + '2 and 3 of a kind  (full)      25.')
    print('   ' + '4 sequential       (small)     30.')
    print('   ' + '5 sequential       (large)     40.')
    print('   ' + '5 of a kind        (yahtzee)   50.')
    print('   ' + 'Any                (chance)    sum of dice.')
    print('   ' + 'There are 13 total turns, and no category')
    print('   ' + 'can be used twice. Additionally, there is')
    print('   ' + 'an upper score that is the sum of the dice,')
    print('   ' + 'which is counted every turn. Call dice in')
    print('   ' + 'the format 1-5 and the way to be graded')
    print('   ' + 'the list above.')
    print('   ' + '-' * 11 + 'Yahtzee Instructions' + '-' * 11)
    print('')


# Define turn.
def turn():
    """Goes through a single turn of the game."""

    # Initialize variables.
    dice, re = [], []

    # Iterate through 3 total dice rolls.
    for i in range(3):
        # On the first roll, roll all dice.
        if i == 0:
            dice += roll(5)
        # On subsequent rolls, allow specific rolling of dice.
        else:
            # Reset variables.
            die, re = 'temp', []

            # Output dice.
            print('   Dice:', dice)

            # Get dice to roll again from input.
            while die != 0:
                # If the user inputs dice 0, stop.
                die = input('   Enter a dice number to roll again (0 to stop): ')

                if die in '0123456789':
                    die = int(die)

                    # Add indexes of dice to a list.
                    if 0 < die <= 5:
                        re.append(die - 1)
            print('')

            # Roll dice again.
            for j in re:
                dice[j] = roll(1)[0]

    # Output and return dice.
    print('   Dice:', dice)
    return dice


# Define roll.
def roll(rolls):
    """Rolls the amount of dice passed through."""

    # Initialize dice.
    dice = []

    # Roll dice according to rolls.
    for i in range(rolls):
        dice.append(randint(1, 6))

    # Return dice.
    return dice


# Define score.
def score(dice, method):
    """Returns the score of the passed dice using the passed method."""

    # Initialize points.
    points = 0

    # Evaluate three of a kind.
    if method == 'three':
        # If there exists three of a kind, add the dice summed.
        for i in range(1, 7):
            if dice.count(i) >= 3:
                points += sum(dice)

    # Evaluate four of a kind.
    elif method == 'four':
        # If there exists four of a kind, add the dice summed.
        for i in range(1, 7):
            if dice.count(i) >= 4:
                points += sum(dice)

    # Evaluate a full house.
    elif method == 'full':
        # If there exists both a two and three of a kind add 25.
        a, b = False, False
        for i in range(1, 7):
            if dice.count(i) == 3:
                a = True
            if dice.count(i) == 2:
                b = True
        if a and b:
            points += 25

    # Evaluate a small sequence.
    elif method == 'small':
        # If there exists a sequence of 4 numbers add 30.
        for i in range(1, 7):
            if dice.count(i) == 2:
                dice.remove(i)
        dice = ''.join(str(i) for i in sorted(dice))
        if '1234' in dice or '2345' in dice or '3456' in dice:
            points += 30

    # Evaluate a large sequence.
    elif method == 'large':
        # If there exists a sequence of 5 numbers add 40.
        dice = ''.join(str(i) for i in sorted(dice))
        if '12345' in dice or '23456' in dice:
            points += 40

    # Evaluate five of a kind.
    elif method == 'yahtzee':
        # If there exists five of a kind, add 50.
        for i in range(1, 7):
            if dice.count(i) == 5:
                points += 50

    # Evaluate a chance.
    elif method == 'chance':
        # Add the dice summed.
        points += sum(dice)

    # Return points.
    return points


# Main Program


# Output an initial message and the instructions.
print('Welcome to Yahtzee!')
instructions()

# Initialize variables.
score1, score2, way, previous, q = 0, 0, '', [], False

# Initialize repeat from input.
repeat = input('Enter "y" to allow repeated scoring methods: ')
print('-' * 100)

# Iterate through the thirteen turns.
for t in range(13):
    # Output the current turn.
    print('TURN', t + 1)

    # Allow the user to view one of several items.
    option = input('   (i: instructions, q: quit, or s: score): ')

    # Output the indicated item
    if option == 'q':
        # Allow the user to quit the game.
        q = True
        break
    elif option == 'i':
        # Allow the user to view the instructions.
        instructions()
    elif option == 's':
        # Allow the user to view the current score.
        print('   Current score:', score1 + score2)
    # Run through a turn, set the dice to final.
    final = turn()

    # Increment score 1 by the dice.
    score1 += sum(final)

    # Ask the user for a way to score.
    way = input('   Enter the way to score (n for none): ')

    # Ensure the method has not been used.
    if way not in previous or repeat == 'y':
        # Add the method to the list of methods used.
        previous.append(way)

        # Increment score 2 by the dice scored with the method.
        score2 += score(final, way)
    print('-' * 100)

# Ensure the user has not quit.
if not q:
    # Add an additional 35 points if score 1 exceeded 63.
    if score1 >= 63:
        score1 += 35

    # Output final scores.
    print('DONE!')
    print('   Upper score:', score1)
    print('   Lower score:', score2)
    print('   Final score:', score1 + score2)

    # Open file for output.
    File = open('Board.txt', 'a')

    # Allow the user to input their name.
    name = input('   Enter a name: ')

    # Write the user's name and score to the file.
    File.write(name + ' Played Yahtzee! with a final score of ' + str(score1 + score2))

    # Close the file.
    File.close()

# Output a final message to the user.
print('-' * 100)
print('Thanks for playing!')
