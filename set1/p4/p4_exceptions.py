# Name: PAUL VINCENT M. PAVO
# Section: IV-BSIT-B
# Activity: P4 - Safe Menu Program
# Date: November 26, 2026

def divide_numbers():
    print("\n=+=+=+= DIVISION =+=+=+=")

    try:
        first_number = float(input("\nEnter the first number: "))
        second_number = float(input("Enter the second number: "))

        result = first_number / second_number

    except ValueError:
        print("\nInvalid input! Bawal yan! Please enter numeric values.")

    except ZeroDivisionError:
        print("\nError! Division by zero is not allowed.")

    else:
        print("\nResult:", result)

    finally:
        print("\nDivision operation finished.")


def open_file():
    print("\n=+=+=+= OPEN FILE =+=+=+=")

    file_name = input("\nEnter the file name: ")

    try:
        with open(file_name, "r") as file:
            contents = file.read()

    except FileNotFoundError:
        print("\nFile not found! Please check the file name.")

    else:
        print("\n=+=+=+= FILE CONTENTS =+=+=+=")
        print(contents)

    finally:
        print("\nFile operation finished.")


def display_menu():
    print("\n=+=+=+= SAFE MENU PROGRAM =+=+=+=\n")
    print("[1] Divide two numbers")
    print("[2] Open and read a file")
    print("[3] Exit")


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice (1, 2, or 3): ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("\nAvisala! Thank you for using the safe menu program!")
            break

        else:
            print("\nInvalid menu choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()