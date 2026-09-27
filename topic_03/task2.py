numbers = [5, 2, 8, 1, 4]

print("Початковий список:", numbers)

numbers.append(10)
print("append:", numbers)

numbers.extend([6, 7])
print("extend:", numbers)

numbers.insert(2, 15)
print("insert:", numbers)

numbers.remove(8)
print("remove:", numbers)

numbers.sort()
print("sort:", numbers)

numbers.reverse()
print("reverse:", numbers)

new_numbers = numbers.copy()
print("copy:", new_numbers)

numbers.clear()
print("clear:", numbers)