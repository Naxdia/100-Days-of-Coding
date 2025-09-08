# # Day 7: Modules and Functions - Hangman Game
# #  Modules are files containing Python code. They can define functions, classes, and variables.

# import random
# from Hangman_List import word_list
# # print(word_list) 

# random_word = random.choice(word_list)
# print(random_word)

# lives = 7

# blank_word = ""
# for letter in random_word:
#     blank_word += "_"
# print(blank_word)

# correct_guesses = []

# while lives > 0:
#     print(blank_word)
#     user_guess = input("Guess a letter.\n").lower()
#     if user_guess in random_word:
#         print(f"You guessed {user_guess}. That's in the word!")
#         correct_guesses.append(user_guess)
#         print(f"Correct guesses so far: {', '.join(correct_guesses)}")
#     else:
#         lives -= 1
#         print(f"You guessed {user_guess}. That's not in the word. You lose a life.")
#         print(f"You have {lives} lives left.")


# if correct_guesses == random_word:
#     print

import random
from Hangman_List import word_list

word_to_guess = random.choice(word_list)
lives = 7
print(word_to_guess)
#Tuples are immatable; we use a list so correct_guesses can be sorted and changed
correct_guesses = []
incorrect_guesses = []
blank_word = ""

for letter in word_to_guess:
    blank_word += "_"

#The first if statement checks if the user has won before asking for a guess
while lives > 0:
    if blank_word == word_to_guess:
        print(f"You win! The word was {word_to_guess}.")
        break
    print(blank_word)
    user_guess = input("Guess a letter.\n").lower()
    if blank_word == word_to_guess:
        print(f"You win! The word was {word_to_guess}.")
        break
    elif user_guess in word_to_guess and user_guess not in correct_guesses:
        print(f"You guessed {user_guess}. That's in the word!")
        # Index refers to the position of the letter in the word, the "," unpacks the enumerate object into index and letter within the for loop and enumerate gives the word_to_guess an index position
        for index, letter in enumerate(word_to_guess):
            #Correctly guessed letter is placed in the blank_word string
            if letter == user_guess:
                # [:index] gets everything before the index, user_guess adds the guessed letter, [index + 1:] gets everything after the index
                blank_word = blank_word[:index] + user_guess + blank_word[index + 1:]
        correct_guesses.append(user_guess)
        correct_guesses = sorted(correct_guesses)
        print(f"Correct guesses so far: {(correct_guesses)}")
    # If the entire word has been guessed correctly

    # If the guessed letter is not in the word and hasn't been guessed before
    elif user_guess not in word_to_guess and user_guess not in incorrect_guesses:
        lives -= 1
        incorrect_guesses.append(user_guess)
        incorrect_guesses = sorted(incorrect_guesses)
        print(f"You guessed {user_guess}. That's not in the word. You lose a life.")
        print(f"You have {lives} lives left.")
        print(f"Incorrect guesses so far: {(incorrect_guesses)}")