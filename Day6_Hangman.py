# Hangman Game
# Hangman is a guessing game for two or more players. One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses. Originally a paper-and-pencil game, there are now electronic versions.
# Doesn't work for now.

# dependencies
import random

word_list = ["renewed", "effortless",
             "certification", "experience", "comparison"]


def hangman():
    # TODO: Randomly choose a word from word list as choosen word, and print it.
    chosen_word = random.choice(word_list)
    print(choosen_word)

    # correct word
    correct_letters = []

    # TODO: Generator placeholder with the same number of choosed word
    # for i in range(len(choosen_word)):
    #     print("_", end=" ")  # Make sure the place holder is in one row.
    # print()
    # Better Method to generate the placeholder
    placeholder = " ".join("_" for _ in range(len(chosen_word)))
    print(placeholder)

    guess_times = len(chosen_word) + 3
    print(
        f"This word has {len(chosen_word)} letters, so you have {guess_times} times to guess.")

    for i in range(guess_times):
        user_guess = input(
            "To start game, guess a letter from a-z: ").strip().lower()
        print(f"Your guess is {user_guess}.")

        # TODO: check the user guess if it is one of the choosen word, print Right if it's right, else print wrong.
        display = ""

        for i in range(len(chosen_word)):
            if chosen_word[i] == user_guess:
                # display += user_guess
                correct_letters.append(user_guess)
            elif chosen_word[i] in correct_letters:
                display += chosen_word[i]
            else:
                display += "_"

        # print display
        print(display)

        # test if user is win
        if "_" not in display:
            print(f"You win.")


# call the function
print("Welcome to Hangman's world")
user_input = input("Do you want to play? Y or N: ").strip().lower()
while True:
    if user_input == "y":
        hangman()
    else:
        print("Bye. Have a wonderful day.")
        break
