students = []  # List to store student records
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = int(input("Enter marks: "))
    student = {"name": name, "roll": roll, "marks": marks}
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
    else:
        print("\nAll Students:")
        for s in students:
            print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
        print()

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found: Name: {s['name']}, Marks: {s['marks']}\n")
            return
    print("Student not found.\n")

def update_marks():
    roll = input("Enter roll number to update marks: ")
    for s in students:
        if s["roll"] == roll:
            new_marks = int(input("Enter new marks: "))
            s["marks"] = new_marks
            print("Marks updated successfully!\n")
            return
    print("Student not found.\n")

def delete_student():
    roll = input("Enter roll number to delete: ")
    for i, s in enumerate(students):
        if s["roll"] == roll:
            del students[i]
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

def main():
    while True:
        print("==== Student Record Manager ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
main()
