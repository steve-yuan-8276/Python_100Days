# Calculate the total price based on customer's choices.

def calculate_price(size, pepperoni, cheese):

    small_pizza_price = 12
    medium_pizza_price = 20
    large_pizza_price = 25
    pepperoni_small_pizza_price = 2
    pepperoni_medium_large_pizza_price = 3
    extra_cheese_price = 1

    total_price = 0

    if size == "S":
        total_price = small_pizza_price
        if pepperoni == "Y":
            total_price += pepperoni_small_pizza_price
        if cheese == "Y":
            total_price += extra_cheese_price
    elif size == "M":
        total_price = medium_pizza_price
        if pepperoni == "Y":
            total_price += pepperoni_medium_large_pizza_price
        if cheese == "Y":
            total_price += extra_cheese_price
    elif size == "L":
        total_price = large_pizza_price
        if pepperoni == "Y":
            total_price += pepperoni_medium_large_pizza_price
        if cheese == "Y":
            total_price += extra_cheese_price

    # return the total price
    return total_price


# Get the infos from customer, including: size of the pizza, pepperoni, extra_cheese
print("Welcome to the Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L: ").strip().upper()
pepperoni = input("Do you want pepperoni? Y or N: ").strip().upper()
cheese = input("Do you want extra cheese? Y or N: ").strip().upper()

# call the function to calculate
total_price = calculate_price(size, pepperoni, cheese)

# print the outputs:
print(f"The total price is {total_price:.2f}")
