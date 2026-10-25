
import requests

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    rates = {}

    for currency in data:
        if currency["cc"] in ["USD", "EUR", "PLN"]:
            rates[currency["cc"]] = currency["rate"]

    print("Доступні валюти: USD, EUR, PLN")

    currency = input("Введіть валюту: ").upper()

    if currency in rates:
        try:
            amount = float(input("Введіть суму: "))

            if amount < 0:
                print("Помилка: сума не може бути від'ємною")
            else:
                result = amount * rates[currency]
                print(f"Курс {currency}: {rates[currency]:.4f} грн")
                print(f"Результат: {result:.2f} грн")

        except ValueError:
            print("Помилка: введіть правильну суму")
    else:
        print("Помилка: невідома валюта")

except (requests.RequestException, ValueError, KeyError) as error:
    print("Помилка отримання курсів валют:", error)