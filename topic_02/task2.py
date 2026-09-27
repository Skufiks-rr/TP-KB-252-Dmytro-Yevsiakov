def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /): ")

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