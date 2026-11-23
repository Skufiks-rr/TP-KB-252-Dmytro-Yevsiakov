
import unittest
import os
import tempfile
from Student import Student
from StudentList import StudentList
from Utils import Utils


class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("Dima", "123456789", "dima@gmail.com", "KB-252")
        self.assertEqual(student.name, "Dima")
        self.assertEqual(student.phone, "123456789")
        self.assertEqual(student.email, "dima@gmail.com")
        self.assertEqual(student.group, "KB-252")

    def test_student_string(self):
        student = Student("Dima", "123", "dima@gmail.com", "KB-252")
        self.assertIn("Dima", str(student))
        self.assertIn("KB-252", str(student))


class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.students = StudentList()
        self.students.add(Student("Bob", "111", "bob@gmail.com", "KB-251"))
        self.students.add(Student("Dima", "222", "dima@gmail.com", "KB-252"))

    def test_add(self):
        self.students.add(Student("Alex", "333", "alex@gmail.com", "KB-253"))
        self.assertEqual(len(self.students.get_all()), 3)
        self.assertEqual(self.students.get_all()[0].name, "Alex")

    def test_delete(self):
        self.assertTrue(self.students.delete("Bob"))
        self.assertEqual(len(self.students.get_all()), 1)

    def test_delete_not_found(self):
        self.assertFalse(self.students.delete("Max"))

    def test_update(self):
        result = self.students.update(
            "Bob", "Max", "999", "max@gmail.com", "KB-254"
        )
        self.assertTrue(result)
        self.assertEqual(self.students.get_all()[-1].name, "Max")

    def test_update_not_found(self):
        self.assertFalse(
            self.students.update("Alex", "Max", "999", "max@gmail.com", "KB-254")
        )


class TestUtils(unittest.TestCase):
    def test_csv_save_and_load(self):
        students = StudentList()
        students.add(Student("Dima", "123", "dima@gmail.com", "KB-252"))
        utils = Utils()

        with tempfile.TemporaryDirectory() as directory:
            filename = os.path.join(directory, "test_students.csv")
            utils.save_to_csv(filename, students)

            loaded = StudentList()
            utils.load_from_csv(filename, loaded)

            self.assertEqual(len(loaded.get_all()), 1)
            self.assertEqual(loaded.get_all()[0].name, "Dima")
            self.assertEqual(loaded.get_all()[0].group, "KB-252")


if __name__ == "__main__":
    unittest.main()
