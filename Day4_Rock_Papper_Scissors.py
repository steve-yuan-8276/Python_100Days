# Game: Rock, Paper, Scissors
# Rule: Game and computer randomly guess a number: R for Rock, P for Paper, S for Scissors
# If gamer = Paper, computer = Rock, then gamer win.
# if gamer = Scissors, computer = Paper, then gamer win.
# if gamer = Rock, computer = Scissors, then gamer win.
# if gamer = computer, then tie.
# else, computer win.

# Dependencies
import random

options = ["Rock", "Paper", "Scissors"]


def RPS_Game(gamer_choice):

    # Computer generate a number
    computer_choice = random.choice(options)

    if (gamer_choice == "Paper" and computer_choice == "Rock") or \
        (gamer_choice == "Scissors" and computer_choice == "Paper") or \
            (gamer_choice == "Rock" and computer_choice == "Scissors"):
        print(
            f"Your choice is {gamer_choice}, and computer choose {computer_choice}. You win.")
    elif gamer_choice == computer_choice:
        print(f"Both of you have the same choice: {gamer_choice}. Tied.")
    else:
        print(
            f"Your choice is {gamer_choice}, and computer choose {computer_choice}.Computer Win.")


gamer_choice = input(
    "Welcome to Rock-Paper-Scissors Game.\n To Start, just make a choice: Rock, Paper, or Scissors. ").strip().title()
# Call the function
RPS_Game(gamer_choice)
