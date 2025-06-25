# This scripts calculates the tip amount based on the total bill and the desired tip percentage.

def calculate_tip():
    # get the total bills amount
    bill = input("Please enter the total bill amount: $ ")

    # get the tip percentage
    tip_percentage = input(
        "Please enter the tip percentage(%): 10, 12, 15, 20: ")

    # Get the number of pepple:
    people_count = input("How many people are sharing the bills?")

    # calculate the total bill including tips
    total_bills = float(bill) * (1 + float(tip_percentage)/100)

    # calculate the cost per person
    cost_per_person = total_bills / int(people_count)

    # return the outputs
    return total_bills, cost_per_person


# Call the function to calculate
total_bills, cost_per_person = calculate_tip()

# print the results
print(f"The total bill amount is ${total_bills: .2f}")
print(f"Each person should pay ${cost_per_person: .2f}")
