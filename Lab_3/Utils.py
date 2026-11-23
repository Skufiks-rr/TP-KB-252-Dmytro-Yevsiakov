import csv
from Student import Student


class Utils:
    def load_from_csv(self, filename, student_list):
        with open(filename, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(
                    row["name"],
                    row["phone"],
                    row["email"],
                    row["group"]
                )
                student_list.add(student)

    def save_to_csv(self, filename, student_list):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "email", "group"])

            for student in student_list.get_all():
                writer.writerow([
                    student.name,
                    student.phone,
                    student.email,
                    student.group
                ])
