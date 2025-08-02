def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'D'

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    math = int(input("Enter Math Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    
    with open("students.txt", "a") as file:
        file.write(f"Roll: {roll} | Name: {name} | Math: {math} | Science: {science} | English: {english}\n")
    print("Student record added successfully!\n")

def view_students():
    print("\n--- Student Records ---")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No records found.")

def search_by_roll():
    roll = input("Enter Roll Number to search: ")
    found = False
    try:
        with open("students.txt", "r") as file:
            for line in file:
                if f"Roll: {roll} " in line:
                    print("\nRecord Found:\n", line.strip())
                    parts = line.strip().split("|")
                    marks = [int(part.split(":")[1].strip()) for part in parts[2:]]
                    avg = sum(marks) / len(marks)
                    grade = calculate_grade(avg)
                    print(f"Average Marks: {avg:.2f}")
                    print(f"Grade: {grade}")
                    found = True
                    break
        if not found:
            print("No record found with that Roll Number.")
    except FileNotFoundError:
        print("No records found.")

def main_menu():
    while True:
        print("\n========= Student Report Card System =========")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Search by Roll Number")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_by_roll()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

main_menu()
