from functions import add, subtract, multiply, divide


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Помилка: введіть число")


def calculate(operation, a, b):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)
    else:
        return "Невідома операція"
