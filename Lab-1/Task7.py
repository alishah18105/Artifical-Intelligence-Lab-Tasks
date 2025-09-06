# Exercise 
# Create a Python Program that perform following tasks for any problem of your choice: that must 
# include 
# Task 1: Introduction 
# Task 2: Terminal 
# Task 3: Python Interpreter 
# Task 4: Variables 
# Task 5: Opertaors 
# Task 6: Dictionary usage 
# Task 7: Lists and Tuples 
# Task 8: Conditional Statements 
# Task 9: The For Loop 
# Task 10: User Input and the While Loop

record = {}

print("============================================================\n")
print("Welcome To The Student Management System")
print("\n============================================================\n")

print("This program helps teachers add students, input marks, calculate grades, and view records.\n\n")
while True:
    print("----------------------------------\n\n")
    print("Main Menu\n")
    print("Please select an option from the menu below:\n")
    print("1. Add Student")
    print("2. View a Student Record")
    print("3. Show All Students")
    print("4. Exit\n")

    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        name = input("Enter student's name: ")
        maths = int(input("Enter marks in Maths: "))
        english = int(input("Enter marks in English: "))
        science = int(input("Enter marks in Science: "))
        computer = int(input("Enter marks in Computer: "))
        record[name] = {
            'Maths': maths,
            'English': english,
            'Science': science,
            'Computer': computer
        }
        print(f"\n{name}'s record added successfully\n")

    elif choice == 2:
        name = input("Enter the student's name to view record: ")
        if name in record:
            print(f"\nRecord for {name}:")
            print("=========================\n")
            for subject, marks in record[name].items():
                print(f"{subject}: {marks}")
    
    elif choice == 3:
        if not record:
            print("\nNo student records found.\n")
        else:
            print("\nAll Student Records:")
            print("=========================\n")
            for name, marks in record.items():
                print(f"Name: {name}")
                for subject, score in marks.items():
                    print(f"{subject}: {score}")
                print("-------------------------")
            
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
