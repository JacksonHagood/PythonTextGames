# game 8

# full text rock paper scissors game
# ai is completely random

from random import randint

# initialize win
won = 0


def cpu():
    """generates the computer's turn"""

    choice = randint(0, 2)
    if choice == 0:
        return 'ROCK'
    elif choice == 1:
        return 'PAPER'
    else:
        return 'SCISSORS'


def check(p, c):
    """returns the winner"""

    if p == 'ROCK' and c == 'SCISSORS':
        return 'p'
    elif p == 'SCISSORS' and c == 'PAPER':
        return 'p'
    elif p == 'PAPER' and c == 'ROCK':
        return 'p'
    elif p == c:
        return 't'
    return 'c'


# introduction
print('\nWelcome to Rock Paper Scissors!'
      '\nYou will play until you lose'
      '\nPlay "rock", "paper" or "scissors"\n')

# run through the game
while True:
    # run the player turn and generate a cpu turn
    player = input('Your Move: ').upper()
    computer = cpu()

    # output the turn and indicate the winner
    if check(player, computer) == 'p':
        print(player.lower(), 'beats', computer.lower())
        print('You Win! :)\n')
        won += 1
    elif check(player, computer) == 't':
        print('both played', player.lower())
        print('Tie\n')
    else:
        print(computer.lower(), 'beats', player.lower())
        print('Game Over! :(')
        break

# output and closing statement
print('\nYou won', won, 'times')
file = open('Board.txt', 'a')
file.write(input('Enter Your Name: ') + ' Won in Rock Paper Scissors ' + str(won) + ' times\n')
file.close()
print('Thanks for playing!')
