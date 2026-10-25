import functions
from operations import get_number, calculate


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

    result = calculate(operation, a, b)
    print("Результат:", result)
