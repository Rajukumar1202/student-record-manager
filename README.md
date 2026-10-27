# 🎓 Student Record Manager

A simple, reliable, and beginner-friendly Student Record Management System built with Python. It allows users to manage student records through a menu-driven command-line interface and stores data locally in JSON format.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/Data-JSON-orange)
![Testing](https://img.shields.io/badge/Tests-10%20Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview

Student Record Manager is a Python project designed to demonstrate fundamental programming concepts, file handling, input validation, and automated testing.

The application helps users create, view, search, update, and delete student records from a local JSON file.

## ✨ Features

- ➕ **Add Students:** Create records with a unique student ID, name, age, and course.
- 📋 **View Records:** Display all students in a formatted table.
- 🔍 **Search Students:** Find a student using their ID.
- ✏️ **Update Records:** Modify existing student information.
- 🗑️ **Delete Records:** Remove records with confirmation.
- 💾 **JSON Storage:** Save records locally and load them when the application starts.
- 🛡️ **Input Validation:** Handle empty fields, invalid ages, and duplicate student IDs.
- 🧪 **Automated Tests:** Test important operations and JSON file handling with Python's built-in `unittest` framework.

## 🛠️ Technologies Used

- **Python 3**
- **JSON** for local data storage
- **Pathlib** for file path handling
- **unittest** for automated testing
- **Git and GitHub** for version control and project hosting

## 📂 Project Structure

```text
student-record-manager/
├── main.py
├── students.json
├── README.md
├── .gitignore
└── tests/
    └── test_student_manager.py
```

| File | Description |
|---|---|
| `main.py` | Main application and student management operations |
| `students.json` | Local student data file; excluded from Git |
| `tests/test_student_manager.py` | Automated unit tests |
| `.gitignore` | Specifies files Git should ignore |
| `README.md` | Project documentation |

## ⚙️ Installation and Setup

### 1. Prerequisites

Install Python 3 and Git on your computer.

Verify Python installation:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/Rajukumar1202/student-record-manager.git
```

### 3. Open the project directory

```bash
cd student-record-manager
```

### 4. Run the application

```bash
python main.py
```

No third-party Python packages are required.

## 🚀 How to Use

When the application starts, a menu appears:

```text
===== STUDENT RECORD MANAGER =====
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

Enter the corresponding menu number and follow the prompts.

### Example Student Record

```json
{
    "id": "ST101",
    "name": "Raju Kumar",
    "age": 20,
    "course": "B.Tech CSE"
}
```

Student records are stored in `students.json` on your local computer.

## 🧪 Running Tests

The project includes automated tests for student operations, input validation, and JSON persistence.

Run the test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The current test suite contains **10 tests**, covering:

- Successful student creation
- Duplicate and empty student IDs
- Invalid ages and empty names
- Successful record updates
- Successful record deletion
- Saving and loading JSON records
- Missing JSON files
- Invalid JSON content

## 🔒 Data and Privacy

Student records are stored locally in `students.json`. This file is excluded from version control through `.gitignore` to help prevent accidental publication of personal data.

**Note:** `.gitignore` does not automatically remove a file that Git is already tracking. Verify repository tracking before publishing sensitive information.

## 🗺️ Future Improvements

Potential enhancements for future versions:

- Separate application logic into modules
- Add student marks and percentage calculations
- Export records to CSV
- Improve table formatting and user experience
- Add more edge-case and failure-handling tests
- Introduce a graphical user interface

## 🎯 Learning Outcomes

This project provides practical experience with:

- Python functions and control flow
- Lists and dictionaries
- Input validation and exception handling
- JSON file operations
- CRUD operations
- Unit testing and mocking
- Git and GitHub workflows

## 👨‍💻 Author

**Raju Kumar**

B.Tech CSE (AI/ML) student and aspiring AI Engineer.

- GitHub: [@Rajukumar1202](https://github.com/Rajukumar1202)
- Project Repository: [Student Record Manager](https://github.com/Rajukumar1202/student-record-manager)

---

⭐ If you find this project useful, consider starring the repository.

*Built as part of my journey to strengthen Python programming and software development fundamentals.*