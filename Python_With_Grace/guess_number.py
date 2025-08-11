# Guess Number

# Rules


# 1.Create a random number

# 2.you have 6 chances to guess

# 3.if guess number=computer number,print("bingo!")

# 4.if your number is lower than computer number print("higher")

# 5.if your number is higher than computer number print("lower")

# 6>if you guess 6 times and you have not guessed it right yet print("you failed better luck next time!")

import random
computer_number = random.randint(1, 100)
# computer_number

tries = 0
# tries

while tries < 10:
    guess_number = int(input("guess a number between 1 and 100: ").strip())
    if guess_number > computer_number:
        print("lower.")
    elif guess_number < computer_number:
        print("higher")
    else:
        print("bingo!")
        break
    tries += 1

if guess_number != computer_number and tries == 10:
    print(
        f"The correct number is {computer_number}.\nyou failed better luck next time!")
