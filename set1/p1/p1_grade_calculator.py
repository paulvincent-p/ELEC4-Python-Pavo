# Name: PAUL VINCENT M. PAVO
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 23, 2026

PASSING_AVERAGE = 75


def get_grade():
    while True:
        text = input("Enter grade (0-100): ")
        if text.replace(".", "", 1).isdigit() and 0 <= float(text) <= 100:
            return float(text)
        print("\nInvalid grade. Try again.\n")


def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(average):
    if average >= PASSING_AVERAGE:
        return "Passed"
    return "Failed"


def main():
    grades = []
    while True:
        print("\n=+=+= Grade Calculator =+=+=")
        print("\n1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("\nChoose: ")

        if choice == "1":
            count = int(input("\nHow many grades? "))
            print()
            grades = []
            for i in range(count):
                grades.append(get_grade())
        elif choice == "2":
            if len(grades) == 0:
                print("\nNo grades entered yet.")
            else:
                average = compute_average(grades)
                print()
                print("Average:", round(average, 2))
                print("Highest:", get_highest(grades))
                print("Lowest:", get_lowest(grades))
                print("Status:", get_status(average))
        elif choice == "3":
            print("\nProgram exited. Goodbye!")
            break
        else:
            print("\nInvalid choice.")


main()

"""
A local variable is created inside a function and can only be used there.
For example, "average" inside main() is local, so get_status() cannot see it
unless it is passed in as a parameter. Yung global variable is created outside
ng mga functions, like PASSING_AVERAGE, so lahat ng function pwede magamit yun or mabasa.

"""