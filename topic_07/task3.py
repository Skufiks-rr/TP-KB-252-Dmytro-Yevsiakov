class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} років"


students = [
    Student("Олена", 19),
    Student("Андрій", 21),
    Student("Марія", 18),
    Student("Богдан", 20),
    Student("Дмитро", 19)
]

print("Сортування за ім'ям:")
for student in sorted(students, key=lambda student: student.name):
    print(student)

print("\nСортування за віком:")
for student in sorted(students, key=lambda student: student.age):
    print(student)