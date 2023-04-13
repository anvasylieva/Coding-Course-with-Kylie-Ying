import random


def play(n):
    i = 0
    while i < n:
        i += 1
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()
        computer = random.choice(['r', 'p', 's'])

        print(f'The user\'s choice is {user} and the computer\'s is {computer}')

        if user == computer:
            print('It\'s a tie')
        #  r > s, s > p, p > r
        elif is_win(user, computer):
            print('The user wins!')
        else:
            print('The computer wins!')


def is_win(player, opponent):
    # return true if player wins
    #  r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


play(int(input(f"Enter the number of games: ")))
