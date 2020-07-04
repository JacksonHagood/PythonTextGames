# game 2

# full text tic tac toe
# 2 player version

# board numbered 0 - 8, like the indexes
board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']


def draw():
    """draws the current board according to filled slots"""

    print('\n+---+---+---+')
    for i in range(9):
        print('| ' + board[i] + ' ', end='')
        if (i + 1) % 3 == 0:
            print('|\n+---+---+---+')


def player(s):
    """runs the players turn by taking input and checking the slot"""

    slot = int(input('\n' + s + "'s move: "))
    if board[slot] in '012345678':
        board[slot] = s
    else:
        print('That space is filled!')


def full():
    """checks if board is full by counting blank slots"""

    count = 0
    for slot in board:
        if slot not in '012345678':
            count += 1
    return count == 9


def win(s):
    """checks to see if given symbol has won"""

    # check across
    for i in range(3):
        if board[0 + 3 * i] == board[1 + 3 * i] == board[2 + 3 * i] == s:
            board[0 + 3 * i] = board[1 + 3 * i] = board[2 + 3 * i] = '#'
            return True

    # check down
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == s:
            board[i] = board[i + 3] = board[i + 6] = '#'
            return True

    # check diagonal right
    if board[0] == board[4] == board[8] == s:
        board[0] = board[4] = board[8] = '#'
        return True

    # check diagonal left
    if board[6] == board[4] == board[2] == s:
        board[6] = board[4] = board[2] = '#'
        return True

    return False


# introduction
print('\nWelcome to Tic Tac Toe!'
      '\n2 player version, X & O'
      '\nBoard is numbered 0 - 8')

# run through the game
while True:
    # draw board and run player turn
    draw()
    player('X')

    # check board and output accordingly
    if win('X'):
        draw()
        print('\nPlayer X Wins')
        break
    elif full():
        draw()
        print('\nTie')
        break

    # run cpu turn
    draw()
    player('O')

    # check board and output accordingly
    if win('O'):
        draw()
        print('\nPlayer O Wins')
        break
    elif full():
        draw()
        print('\nTie')
        break

# closing statement
print('Thanks for playing!')
