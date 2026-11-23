from Student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)
        self.students.sort(key=lambda item: item.name)

    def delete(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def update(self, name, new_name, phone, email, group):
        for student in self.students:
            if student.name == name:
                student.name = new_name
                student.phone = phone
                student.email = email
                student.group = group
                self.students.sort(key=lambda item: item.name)
                return True
        return False

    def print_all(self):
        for student in self.students:
            print(student)

    def get_all(self):
        return self.students
