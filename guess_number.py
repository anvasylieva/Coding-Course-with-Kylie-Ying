import random


def guess(x: int):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Please, enter number between 1 and {x}: "))
        # print(guess, random_number)
        if guess < random_number:
            print("Sorry, guess again. Too low...")
        elif guess > random_number:
            print("Sorry, guess again. Too high...")
    print(f"Yey, congrats. You have guessed the number {random_number} correctly!")


# def computer_guess(x: int):
#     user_number = int(input(f"Please, enter number between 1 and {x}: "))
#     guess = random.randint(1, x)
#     print(guess)
#     while guess != user_number:
#         if guess < user_number:
#             print("Sorry, guess again. Too low...")
#             guess = random.randint(user_number, x)
#             print(guess)
#         elif guess > user_number:
#             print("Sorry, guess again. Too high...")
#             guess = random.randint(1, user_number)
#             print(guess)
#     print(f"Yey, congrats. Computer have guessed the user number {user_number} correctly!")

def computer_guess(x):
    low = 1
    high = x
    response = ""
    while response.upper() != "C":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        response = input(f"Is {guess} number too high (H), too low (L) or correct (C)?: ")
        if response.upper() == "H":
            high = guess - 1
        if response.upper() == "L":
            low = guess + 1
    print(f"Yey, the computer has guessed your number {guess} correctly!")


# guess(10)
computer_guess(1000)
