def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: ділення на нуль"


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Помилка: введіть число")


while True:
    operation = input("Введіть операцію (+, -, *, /) або exit: ")

    if operation == "exit":
        print("Програму завершено")
        break

    if operation not in ["+", "-", "*", "/"]:
        print("Невідома операція")
        continue

    a = get_number("Введіть перше число: ")
    b = get_number("Введіть друге число: ")

    if operation == "+":
        print("Результат:", add(a, b))
    elif operation == "-":
        print("Результат:", subtract(a, b))
    elif operation == "*":
        print("Результат:", multiply(a, b))
    elif operation == "/":
        print("Результат:", divide(a, b))