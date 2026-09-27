student = {
    "name": "Dmytro",
    "age": 18,
    "group": "KB-252"
}

print("Початковий словник:", student)

student.update({"city": "Chernihiv"})
print("update:", student)

del student["age"]
print("del:", student)

print("keys:", student.keys())

print("values:", student.values())

print("items:", student.items())

student.clear()
print("clear:", student)