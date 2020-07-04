# game 9

# full text sticks
# ai is completely random

import random

plaL = ['|', ' ', ' ', ' ', ' ']
plaR = ['|', ' ', ' ', ' ', ' ']
cpuL = ['|', ' ', ' ', ' ', ' ']
cpuR = ['|', ' ', ' ', ' ', ' ']


def draw(pl, pr, cl, cr):
    # draws the current board according to filled slots
    print('CPU'.center(25, '-'))
    for i in range(1, 6):
        print(cl[-i], end=' ')
    print(' ' * 5, end='')
    for i in cr:
        print(i, end=' ')
    print('\n')
    for i in range(1, 6):
        print(pl[-i], end=' ')
    print(' ' * 5, end='')
    for i in pr:
        print(i, end=' ')
    print('')
    print('Player'.center(25, '-'))


def check(h):
    # returns true if given hand empty
    if '|' not in h:
        return True
    return False


def move(fr, to):
    # executes a move
    count = (fr.count('|') + to.count('|')) % 5
    for i in range(5):
        to[i] = ' '
        if i < count:
            to[i] = '|'
    return to


# introduction
print('')
print('Welcome to Sticks!')
print('You can pick a hand or split')
print('Pick a player and cpu hand')
print("'l' for left")
print("'r' for left")
print('')

while True:
    draw(plaL, plaR, cpuL, cpuR)

    loc = input('Your Move: ').upper()
    des = input('Their Hand: ').upper()
    print('')

    if loc == 'L' and des == 'L':
        cpuL = move(plaL, cpuL)
    elif loc == 'L' and des == 'R':
        cpuR = move(plaL, cpuR)
    elif loc == 'R' and des == 'L':
        cpuL = move(plaR, cpuL)
    elif loc == 'R' and des == 'R':
        cpuR = move(plaR, cpuR)

    if check(cpuL) and check(cpuR):
        print('You Win! :)')
        file = open('Board.txt', 'a')
        file.write(input('Enter Your Name: ') + ' Won in Sticks\n')
        file.close()
        break

    loc = random.randint(0, 1)
    des = random.randint(0, 1)

    if loc == 0 and des == 0:
        plaL = move(cpuL, plaL)
    elif loc == 0 and des == 1:
        plaR = move(cpuL, plaR)
    elif loc == 1 and des == 0:
        plaL = move(cpuR, plaL)
    elif loc == 1 and des == 1:
        plaR = move(cpuR, plaR)

    if check(plaL) and check(plaR):
        print('Game Over! :(')
        break

print('Thanks for playing!')
