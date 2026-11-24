# Name: PAUL VINCENT M. PAVO
# Section: IV-BSIT-B
# Activity: P2 - Custom Module
# Date: November 24, 2026

# Import the entire custom module
import student_utils

# Import the functions from the custom module
from student_utils import calculate_average, is_passing

# Import a built-in Python module
from datetime import datetime


# Ask the user how many grades they want to enter
print("===== STUDENT GRADE REPORT =====")
print("Enter your grades (0-100).")

grades = []

number_of_grades = int(input("How many grades will you enter?: "))

# Collect grades from the user
for i in range(number_of_grades):
    grade = float(input(f"Enter grade {i + 1}: "))

    while grade < 0 or grade > 100:
        print("Invalid grade. Please enter a grade from 0 to 100.")
        grade = float(input(f"Enter grade {i + 1} again: "))

    grades.append(grade)


# Use the imported module to get the highest and lowest grades
highest = student_utils.get_highest(grades)
lowest = student_utils.get_lowest(grades)

# Use the imported individual functions
average = calculate_average(grades)
status = is_passing(average)

# Get the current date and time using datetime
report_date = datetime.now()


# Display the student grade report
print("\n===== GRADE REPORT =====")
print("Grades:", grades)
print(f"Average: {average:.2f}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")

if status:
    print("Status: PASSED")
else:
    print("Status: FAILED")

print("Report Generated:", report_date.strftime("%B %d, %Y %I:%M %p"))
