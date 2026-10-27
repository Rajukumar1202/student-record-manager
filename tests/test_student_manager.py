
import json
import tempfile
import unittest
from pathlib import Path
from io import StringIO
from unittest.mock import patch

import main


class TestStudentRecordManager(unittest.TestCase):

    def setUp(self):
        self.students = [
            {
                "id": "ST101",
                "name": "Raju Kumar",
                "age": 20,
                "course": "B.Tech CSE"
            }
        ]

    def test_add_student_successfully(self):
        inputs = ["ST102", "Amit Kumar", "21", "B.Tech AI"]

        with patch("builtins.input", side_effect=inputs), \
             patch.object(main, "save_students", return_value=True):
            main.add_student(self.students)

        self.assertEqual(len(self.students), 2)
        self.assertEqual(self.students[1]["id"], "ST102")
        self.assertEqual(self.students[1]["name"], "Amit Kumar")

    def test_duplicate_student_id_is_rejected(self):
        inputs = ["st101"]

        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new_callable=StringIO):
            main.add_student(self.students)

        self.assertEqual(len(self.students), 1)

    def test_empty_student_id_is_rejected(self):
        inputs = ["   "]

        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new_callable=StringIO):
            main.add_student(self.students)

        self.assertEqual(len(self.students), 1)

    def test_invalid_age_is_rejected(self):
        inputs = ["ST102", "Amit Kumar", "abc"]

        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new_callable=StringIO):
            main.add_student(self.students)

        self.assertEqual(len(self.students), 1)

    def test_empty_student_name_is_rejected(self):
        inputs = ["ST102", "   "]

        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new_callable=StringIO):
            main.add_student(self.students)

        self.assertEqual(len(self.students), 1)

    def test_update_student_successfully(self):
        inputs = ["ST101", "Raju Updated", "21", "B.Tech AI"]

        with patch("builtins.input", side_effect=inputs), \
             patch.object(main, "save_students", return_value=True):
            main.update_student(self.students)

        self.assertEqual(self.students[0]["name"], "Raju Updated")
        self.assertEqual(self.students[0]["age"], 21)
        self.assertEqual(self.students[0]["course"], "B.Tech AI")

    def test_delete_student_successfully(self):
        inputs = ["ST101", "y"]

        with patch("builtins.input", side_effect=inputs), \
             patch.object(main, "save_students", return_value=True):
            main.delete_student(self.students)

        self.assertEqual(len(self.students), 0)

    def test_save_and_load_students(self):
        sample_students = [
            {
                "id": "ST201",
                "name": "Amit Kumar",
                "age": 20,
                "course": "B.Tech CSE"
            }
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "students.json"

            with patch.object(main, "DATA_FILE", test_file):
                self.assertTrue(main.save_students(sample_students))
                loaded_students = main.load_students()

        self.assertEqual(loaded_students, sample_students)

    def test_load_students_when_file_does_not_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "missing.json"

            with patch.object(main, "DATA_FILE", test_file):
                self.assertEqual(main.load_students(), [])

    def test_load_students_with_invalid_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = Path(temp_dir) / "students.json"
            test_file.write_text("{invalid json", encoding="utf-8")

            with patch.object(main, "DATA_FILE", test_file), \
                 patch("sys.stdout", new_callable=StringIO):
                loaded_students = main.load_students()

        self.assertEqual(loaded_students, [])


if __name__ == "__main__":
    unittest.main()
