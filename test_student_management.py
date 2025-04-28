import unittest
from unittest.mock import patch, mock_open
import json

from Student_Management import (
    Student,
    add_student,
    view_students,
    update_student,
    delete_student,
    save_students_to_file,
    load_students_from_file
)

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student(1, "Alice", 16, "VG", ["Math", "Science"]),
            Student(2, "Bob", 17, "G", ["History", "English"])
        ]
        self.student_json = json.dumps([s.to_dict() for s in self.students])

    def test_student_to_dict(self):
        student = Student(1, "Test", 18, "G", ["Art"])
        self.assertEqual(student.to_dict()["name"], "Test")

    def test_update_student_info(self):
        student = self.students[0]
        student.update_student_info(name="Updated", age=17)
        self.assertEqual(student.name, "Updated")
        self.assertEqual(student.age, 17)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_students_to_file(self, mock_file):
        save_students_to_file(self.students)
        mock_file().write.assert_called()

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_load_students_empty(self, mock_file):
        result = load_students_from_file()
        self.assertEqual(result, [])

    @patch("builtins.input", side_effect=["3", "Charlie", "15", "VG", "Math,Science"])
    @patch("Student_Management.save_students_to_file")
    @patch("Student_Management.load_students_from_file", return_value=[])
    def test_add_student(self, mock_load, mock_save, mock_input):
        add_student()
        self.assertTrue(mock_save.called)

    @patch("Student_Management.load_students_from_file", return_value=[])
    def test_view_students_empty(self, mock_load):
        with patch("builtins.print") as mock_print:
            view_students()
            mock_print.assert_called_with("No students found.")

    @patch("builtins.input", side_effect=["1", "Updated", "18", "VG", "Biology"])
    @patch("Student_Management.save_students_to_file")
    @patch("Student_Management.load_students_from_file")
    def test_update_student(self, mock_load, mock_save, mock_input):
        mock_load.return_value = self.students.copy()
        update_student()
        self.assertTrue(mock_save.called)
        self.assertEqual(mock_load.return_value[0].name, "Updated")

    @patch("builtins.input", side_effect=["1"])
    @patch("Student_Management.save_students_to_file")
    @patch("Student_Management.load_students_from_file")
    def test_delete_student(self, mock_load, mock_save, mock_input):
        mock_load.return_value = self.students.copy()
        delete_student()
        self.assertTrue(mock_save.called)
        self.assertEqual(len(mock_save.call_args[0][0]), 1)

if __name__ == "__main__":
    unittest.main()
