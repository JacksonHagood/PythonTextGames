# game 3

# full text tic tac toe
# 2 player version
# board numbered differently

filled = ['temp', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def draw(board):
    # draws the current board according to filled slots
    print('')
    print('-' * 15)
    print('|    ' + board[7] + '|' + board[8] + '|' + board[9] + '    |')
    print('|    ' + '-' * 5 + '    |')
    print('|    ' + board[4] + '|' + board[5] + '|' + board[6] + '    |')
    print('|    ' + '-' * 5 + '    |')
    print('|    ' + board[1] + '|' + board[2] + '|' + board[3] + '    |')
    print('-' * 15)
    print('')


def check(board, slot):
    # checks if slot is blank
    return board[slot] == ' ' and not slot == 0


def player(s):
    # runs the players turn
    slot = int(input('Your move ' + s + ': '))
    if check(filled, slot):
        filled[slot] = s
    else:
        print('That space is filled!')


def full(board):
    # checks if board is full
    count = 0
    for slot in board:
        if slot != ' ':
            count += 1
    return count == 10


def win(b, s):
    # checks to see if given symbol has won
    return ((b[7] == s and b[8] == s and b[9] == s) or
            (b[4] == s and b[5] == s and b[6] == s) or
            (b[1] == s and b[2] == s and b[3] == s) or
            (b[1] == s and b[4] == s and b[7] == s) or
            (b[2] == s and b[5] == s and b[8] == s) or
            (b[3] == s and b[6] == s and b[9] == s) or
            (b[7] == s and b[5] == s and b[3] == s) or
            (b[1] == s and b[5] == s and b[9] == s))


# introduction
print('')
print('Welcome to Tic Tac Toe!')
print('The two players are X and O')
print('The board is numbered as:')
print('')
print('-' * 15)
print('|    7|8|9    |')
print('|    ' + '-' * 5 + '    |')
print('|    4|5|6    |')
print('|    ' + '-' * 5 + '    |')
print('|    1|2|3    |')
print('-' * 15)
print('')

while True:
    # runs through the game
    player('X')
    draw(filled)

    if win(filled, 'X'):
        print('X Wins! :)')
        break
    elif full(filled):
        print('Tie')
        break

    player('O')
    draw(filled)
    if win(filled, 'O'):
        print('O Wins! :)')
        break
    elif full(filled):
        print('Tie')
        break

print('Thanks for playing!')
