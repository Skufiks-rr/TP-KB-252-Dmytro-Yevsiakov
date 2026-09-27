def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


while True:
    operation = input("Введіть операцію (+, -, *, /) або exit: ")

    if operation == "exit":
        print("Програму завершено")
        break

    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))

    if operation == "+":
        print("Результат:", add(a, b))
    elif operation == "-":
        print("Результат:", subtract(a, b))
    elif operation == "*":
        print("Результат:", multiply(a, b))
    elif operation == "/":
        if b != 0:
            print("Результат:", divide(a, b))
        else:
            print("Помилка: ділення на нуль")
    else:
        print("Невідома операція")