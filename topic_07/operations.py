from functions import Calculator


class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()

    def get_number(self, message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Помилка: введіть число")

    def run(self):
        while True:
            operation = input("Введіть операцію (+, -, *, /) або exit: ")

            if operation == "exit":
                print("Програму завершено")
                break

            if operation not in ["+", "-", "*", "/"]:
                print("Невідома операція")
                continue

            a = self.get_number("Введіть перше число: ")
            b = self.get_number("Введіть друге число: ")

            result = self.calculator.calculate(operation, a, b)
            print("Результат:", result)
