def find_position(numbers, value):
    for i in range(len(numbers)):
        if value <= numbers[i]:
            return i

    return len(numbers)


numbers = [1, 3, 5, 7, 9]

value = int(input("Введіть нове число: "))

position = find_position(numbers, value)

print("Позиція для вставки:", position)