
import logging
from pathlib import Path
from operations import get_number, calculate

logging.basicConfig(
    filename=Path(__file__).with_name("calculator.log"),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

while True:
    operation = input("Введіть операцію (+, -, *, /) або exit: ")
    logging.info("Введена операція: %s", operation)

    if operation == "exit":
        logging.info("Завершення роботи програми")
        print("Програму завершено")
        break

    if operation not in ["+", "-", "*", "/"]:
        logging.warning("Невідома операція: %s", operation)
        print("Невідома операція")
        continue

    a = get_number("Введіть перше число: ")
    b = get_number("Введіть друге число: ")

    logging.info("Введені дані: a=%s, b=%s", a, b)

    result = calculate(operation, a, b)

    logging.info("Обчислення: %s %s %s = %s", a, operation, b, result)
    print("Результат:", result)
