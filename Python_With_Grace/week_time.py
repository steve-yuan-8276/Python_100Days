# Calculate how many minutes are in a week?

# TODO: How many days are in a week?
days = input("How many days are in a week? \nPlease enter the number: ")
# TODO: How many hours are in a day?
hours = input(
    "how many hours are in a day? \nPlease enter the correct answer: ")
# TODO: How many minutes are in a hour?
minutes = input(
    "How many minutes are in a hour? \nPlease enter the correct answer: ")
# TODO: convert days hours and minutes format from string into number
days = int(days)
hours = int(hours)
minutes = int(minutes)
# TODO: Formula: calculation
total_minutes = minutes * hours * days
# TODO: Print the results.
print(f"There are {total_minutes} minutes in a week.")
