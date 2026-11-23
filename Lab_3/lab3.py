from sys import argv
from Student import Student
from StudentList import StudentList
from Utils import Utils


def main():
    if len(argv) < 2:
        print("Please specify CSV file name")
        return

    filename = argv[1]
    students = StudentList()
    utils = Utils()

    try:
        utils.load_from_csv(filename, students)
        print("Students loaded from CSV")
    except FileNotFoundError:
        print("CSV file not found")
        return

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")

        match choice.upper():
            case "C":
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter student email: ")
                group = input("Please enter student group: ")

                students.add(Student(name, phone, email, group))
                print("New element has been added")
                students.print_all()

            case "U":
                name = input("Please enter name to be updated: ")

                if any(student.name == name for student in students.get_all()):
                    new_name = input("Please enter new student name: ")
                    phone = input("Please enter new student phone: ")
                    email = input("Please enter new student email: ")
                    group = input("Please enter new student group: ")

                    students.update(name, new_name, phone, email, group)
                    print("Element has been updated")
                    students.print_all()
                else:
                    print("Element was not found")

            case "D":
                name = input("Please enter name to be deleted: ")

                if students.delete(name):
                    print("Element has been deleted")
                else:
                    print("Element was not found")

            case "P":
                print("List will be printed")
                students.print_all()

            case "X":
                utils.save_to_csv(filename, students)
                print("Students saved to CSV")
                print("Exit()")
                break

            case _:
                print("Wrong choice")


if __name__ == "__main__":
    main()
