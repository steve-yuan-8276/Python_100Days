# Tips Calculator

# TODO: How much did you spend on your dishes?
dishes = input("How much did you spend on your dishes?\nPlease enter here: ")
# TODO: How much tips do you want to pay? 15%, 18%, 20%
tip = input(
    "how many tips do you want to pay?\n15%,18% or 20%? Please enter here: ")
# TODO: How many people do you have?
people = input("how many people are in your party?\n Please enter here: ")
# TODO: Calculation: (dishes_spent + dishes_spent * Tips) / number_people
dishes = float(dishes)
tip = float(tip)/100
people = int(people)
# TODO: print the answer
answer = round((dishes + dishes * tip) / people, 2)
print(f"Each of you would spend {answer} bucks! ")
