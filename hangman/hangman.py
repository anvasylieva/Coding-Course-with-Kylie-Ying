import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_words(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or " " in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_words(words).upper()
    # print(word)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in a word!")
        elif user_letter in used_letters:
            print("You have already tried it. Please try again.")
        else:
            print("Invalid character. Please try again.")

        # letters used
        # ' '.joint(['a', 'b', 'cd']) --> 'a b cd'
        print("You have used these letters: ", ''.join(used_letters))
        print(f"You have only {lives} lives.")
        print(lives_visual_dict[lives])
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',  ' '.join(word_list))

    # get here when len(word_letters) == 0 or lives == 0
    if lives > 0:
        print("Congrats. You have guessed the word!")
    else:
        print(f"Sorry, you died, the word was {word}!!!")


hangman()
