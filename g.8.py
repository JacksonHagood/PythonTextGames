# game 8

# full text rock paper scissors game
# ai is completely random

import random

# won holds the amount of wins the player holds
won = 0


def cpu():
    # calculates the computer's turn
    choice = random.randint(0, 2)
    if choice == 0:
        return 'ROCK'
    elif choice == 1:
        return 'PAPER'
    else:
        return 'SCISSORS'


def check(p, c):
    # returns the winner
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
print('')
print('Welcome to Rock Paper Scissors!')
print('You will play until you lose')
print('Play "rock", "paper" or "scissors"')
print('')

while True:
    # runs through the game
    player = input('Your Move: ').upper()
    computer = cpu()
    if check(player, computer) == 'p':
        print(player.lower(), 'beats', computer.lower())
        print('You Win! :)')
        won += 1
    elif check(player, computer) == 't':
        print('both played', player.lower())
        print('Tie')
    else:
        print(computer.lower(), 'beats', player.lower())
        print('Game Over! :(')
        break
    print('-' * 100)

print('\nYou won', won, 'times')
print('Thanks for playing!')
