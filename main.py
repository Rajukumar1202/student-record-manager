
import json
from pathlib import Path

DATA_FILE = Path("students.json")


def load_students():
    """Load student records from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student data.")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        return True
    except OSError:
        print("Error: Student data could not be saved.")
        return False



def add_student(students):
    print("\n--- Add New Student ---")

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    # Check whether this ID already exists.
    for student in students:
        if student["id"].lower() == student_id.lower():
            print("This student ID already exists.")
            return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter student age: ").strip())

        if age <= 0:
            print("Age must be greater than zero.")
            return
    except ValueError:
        print("Invalid age. Please enter a whole number.")
        return

    course = input("Enter student course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    if save_students(students):
        print("Student added successfully!")
    else:
        # Roll back the in-memory change if saving fails.
        students.pop()


def view_students(students):
    print("\n--- All Student Records ---")

    if not students:
        print("No student records found.")
        return

    print("-" * 65)
    print(f"{'ID':<12} {'Name':<22} {'Age':<6} {'Course':<20}")
    print("-" * 65)

    for student in students:
        print(
            f"{student['id']:<12} "
            f"{student['name']:<22} "
            f"{student['age']:<6} "
            f"{student['course']:<20}"
        )

    print("-" * 65)
    print(f"Total students: {len(students)}")



def search_student(students):
    print("\n--- Search Student ---")

    student_id = input("Enter student ID to search: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"].lower() == student_id.lower():
            print("\nStudent Found!")
            print("-" * 30)
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")
            print("-" * 30)
            return

    print("Student not found.")


def update_student(students):
    print("\n--- Update Student ---")

    student_id = input("Enter student ID to update: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student["id"].lower() == student_id.lower():
            print(f"Student found: {student['name']}")
            print("Press Enter to keep the existing value.")

            new_name = input(
                f"Name [{student['name']}]: "
            ).strip()

            new_age = input(
                f"Age [{student['age']}]: "
            ).strip()

            new_course = input(
                f"Course [{student['course']}]: "
            ).strip()

            if new_age:
                try:
                    age_value = int(new_age)
                    if age_value <= 0:
                        print("Age must be greater than zero.")
                        return
                except ValueError:
                    print("Invalid age. Enter a whole number.")
                    return
            else:
                age_value = student["age"]

            updated_student = student.copy()

            if new_name:
                updated_student["name"] = new_name

            updated_student["age"] = age_value

            if new_course:
                updated_student["course"] = new_course

            # Save the previous record for rollback.
            original_student = student.copy()
            student.update(updated_student)

            if save_students(students):
                print("Student updated successfully!")
            else:
                student.clear()
                student.update(original_student)

            return

    print("Student not found.")


def delete_student(students):
    print("\n--- Delete Student ---")

    student_id = input("Enter student ID to delete: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    for index, student in enumerate(students):
        if student["id"].lower() == student_id.lower():
            print(f"Student: {student['name']} (ID: {student['id']})")

            confirm = input(
                "Are you sure you want to delete this student? (y/n): "
            ).strip().lower()

            if confirm != "y":
                print("Delete cancelled.")
                return

            deleted_student = students.pop(index)

            if save_students(students):
                print("Student deleted successfully!")
            else:
                students.insert(index, deleted_student)
                print("Delete failed; original record restored.")

            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students) 
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
