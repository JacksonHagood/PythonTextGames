# game 9

# full text sticks
# ai is completely random

from random import randint

# store player hands each as lists
plaL = ['|', ' ', ' ', ' ', ' ']
plaR = ['|', ' ', ' ', ' ', ' ']
cpuL = ['|', ' ', ' ', ' ', ' ']
cpuR = ['|', ' ', ' ', ' ', ' ']


def draw(pl, pr, cl, cr):
    """draws the current board according to filled slots"""

    # draw the cpu's hands
    print('\n' + 'CPU'.center(25, '-'))
    for i in range(1, 6):
        print(cl[-i], end=' ')
    print(' ' * 5, end='')
    for i in cr:
        print(i, end=' ')

    print('\n')

    # draw the player's hands
    for i in range(1, 6):
        print(pl[-i], end=' ')
    print(' ' * 5, end='')
    for i in pr:
        print(i, end=' ')
    print('\n' + 'Player'.center(25, '-'))


def check(h):
    """returns true if given hand empty"""

    if '|' not in h:
        return True
    return False


def move(fr, to):
    """executes a move"""

    count = (fr.count('|') + to.count('|')) % 5
    for i in range(5):
        to[i] = ' '
        if i < count:
            to[i] = '|'
    return to


# introduction
print('\nWelcome to Sticks!'
      '\nYou can pick a hand or split'
      '\nPick a player and cpu hand'
      "\n'l' for left"
      "\n'r' for left")

# run through the game
while True:
    # draw the board and run the player turn
    draw(plaL, plaR, cpuL, cpuR)
    loc = input('\nYour Move: ').upper()
    des = input('Their Hand: ').upper()
    if loc == 'L' and des == 'L':
        cpuL = move(plaL, cpuL)
    elif loc == 'L' and des == 'R':
        cpuR = move(plaL, cpuR)
    elif loc == 'R' and des == 'L':
        cpuL = move(plaR, cpuL)
    elif loc == 'R' and des == 'R':
        cpuR = move(plaR, cpuR)

    # check for a win and output accordingly
    if check(cpuL) and check(cpuR):
        print('\nYou Win! :)')
        file = open('Board.txt', 'a')
        file.write(input('Enter Your Name: ') + ' Won in Sticks\n')
        file.close()
        break

    # run the cpu turn
    loc = randint(0, 1)
    des = randint(0, 1)
    if loc == 0 and des == 0:
        plaL = move(cpuL, plaL)
    elif loc == 0 and des == 1:
        plaR = move(cpuL, plaR)
    elif loc == 1 and des == 0:
        plaL = move(cpuR, plaL)
    elif loc == 1 and des == 1:
        plaR = move(cpuR, plaR)

    # check for a loss and output accordingly
    if check(plaL) and check(plaR):
        print('\nGame Over! :(')
        break

# closing statement
print('Thanks for playing!')
