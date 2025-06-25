# Generate password based on user's preference

# Dependence
import random

# # Define a function


def pwd_generator(nr_letters, nr_symbols, nr_numbers):
    # default setting
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '_', '-', '*', '+']

    # create a list to store password
    pwds = []

    for _ in range(nr_letters):
        pwd_letter = random.choice(letters)
        pwds.append(pwd_letter)

    for _ in range(nr_numbers):
        pwd_number = random.choice(numbers)
        pwds.append(pwd_number)

    for _ in range(nr_symbols):
        pwd_symbol = random.choice(symbols)
        pwds.append(pwd_symbol)

    # using random.shuffle to randomised list order.
    random.shuffle(pwds)

    # convert the list into string
    pwd_final = ''.join(str(pwd) for pwd in pwds)

    return pwd_final


# Introduction
while True:
    user_input = input(
        "Welcome to the PyPassword Generator!\nDo you want to generate the password: Y or N? ").strip().upper()
    if user_input == "Y":
        nr_letters = int(
            input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        print(
            f"Your password is {pwd_generator(nr_letters, nr_symbols, nr_numbers)}.")
    else:
        print("Bye! See you next time.")
        break
    break
