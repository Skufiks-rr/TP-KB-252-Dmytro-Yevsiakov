class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Помилка: ділення на нуль"
        return a / b

    def calculate(self, operation, a, b):
        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        return operations[operation](a, b)