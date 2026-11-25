# Name: PAUL VINCENT M. PAVO
# Section: IV-BSIT-B
# Activity: P3 - Record Manager
# Date: November 25, 2026

# nag iistore ng student names
students = []

# nakalowercase yung sinesave nito para di magkaduplicate
student_names = set()


def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    if name.lower() in student_names:
        print("This student already exists. Ayun isa pa po!")
    else:
        students.append(name)
        student_names.add(name.lower())
        print(f"{name} has been added successfully.")


def remove_student():
    name = input("Enter the student name to remove: ").strip()

    if name.lower() in student_names:
        for student in students:
            if student.lower() == name.lower():
                students.remove(student)
                student_names.remove(name.lower())
                print(f"{student} has been removed successfully.")
                return
    else:
        print("Student not found.")


def search_student():
    name = input("Enter student name: ").strip().lower()

    if name == "":
        print("Please enter a name to search.")
        return

    found_students = []

    for student in students:
        if name in student.lower():
            found_students.append(student)

    if found_students:
        print("\n===== SEARCH RESULTS =====")
        for student in found_students:
            print(student)
        print(f"Total matches: {len(found_students)}")
    else:
        print("No matching student found.")


def display_students():
    if len(students) == 0:
        print("No students in the record.")
        return

    sorted_students = sorted(students, key=str.lower)

    print("\n===== STUDENT RECORDS =====")

    for index, student in enumerate(sorted_students, start=1):
        print(f"{index}. {student}")

    print(f"\nTotal students: {len(students)}")


def show_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")


while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you! Come again. Matsala geng!")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")


# Difference between a list and a set:

# Kapag list, nag istore siya ng multiple items tapos kung pano yung order nya ganun pa rin, 
# pero pag set naman, nagi-store siya ng unique items tapos automatic na pine-prevent yung duplicates
# So dito, I used list to store and display the original student names.
# I used set naman for containing lowercase names to check for duplicates.
