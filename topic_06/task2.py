students = [
    {"name": "Олена", "grade": 92},
    {"name": "Андрій", "grade": 78},
    {"name": "Марія", "grade": 95},
    {"name": "Богдан", "grade": 85},
    {"name": "Дмитро", "grade": 90}
]

by_name = sorted(students, key=lambda student: student["name"])
by_grade = sorted(students, key=lambda student: student["grade"])

print("Сортування за ім'ям:")
for student in by_name:
    print(student["name"], "-", student["grade"])

print("\nСортування за оцінкою:")
for student in by_grade:
    print(student["name"], "-", student["grade"])
