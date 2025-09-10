# TODO: What is the lowest temprature today in F
lowest_temprature = input(
    "What is the lowest temprature today in fahrenhiets: ")
# TODO: What is the highest temprature today in F
highest_temprature = input(
    "What is the highest temprature today in fahrenhiets: ")
# TODO: Convert lowest temprature and highest temprature from int to float
lowest_temprature = float(lowest_temprature)
highest_temprature = float(highest_temprature)
# TODO: Formula: calculation
# Use Round to keep one dicimal
lowest_temprature_C = round(5/9 * (lowest_temprature - 32), 1)
highest_temprature_C = round(5/9 * (highest_temprature - 32), 1)
# TODO: Print the results
print(
    f" The lowest temprature is {lowest_temprature_C} ℃ and the highest temprature is {highest_temprature_C} ℃. ")
