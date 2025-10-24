def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")


def subtract(a, b):
    result = a - b
    print(f"{a} - {b} = {result}")


def multiply(a, b):
    result = a * b
    print(f"{a} x {b} = {result} ")


def divide(a, b):
    result = a / b
    print(f"{a} % {b} = {result}")


a = input("Please enter a number: ")
b = input("please enter a number: ")

a = int(a)
b = int(b)

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
