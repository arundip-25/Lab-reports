students = []

def add_student():
    if len(students) >= 20:
        print("Maximum student limit reached.")
        return
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    subjects = {}
    sub_list = ["Math", "Science", "English"]
    for sub in sub_list:
        marks = int(input(f"Enter marks in {sub}: "))
        subjects[sub] = marks
    students.append({"name": name, "roll": roll, "marks": subjects})
    print("Student added successfully.")

def view_all_reports():
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(f"\nName: {s['name']}")
        print(f"Roll No.: {s['roll']}")
        for sub, mark in s['marks'].items():
            print(f"{sub}: {mark}")
        avg = sum(s['marks'].values()) / len(s['marks'])
        print(f"Average: {avg:.2f}")

def display_topper():
    if not students:
        print("No student records found.")
        return
    top_avg = -1
    toppers = []
    for s in students:
        avg = sum(s['marks'].values()) / len(s['marks'])
        if avg > top_avg:
            top_avg = avg
            toppers = [s]
        elif avg == top_avg:
            toppers.append(s)
    print(f"\nTopper(s) with average {top_avg:.2f}:")
    for t in toppers:
        print(f"Name: {t['name']} | Roll No.: {t['roll']}")

def search_by_roll():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"\nName: {s['name']}")
            print(f"Roll No.: {s['roll']}")
            for sub, mark in s['marks'].items():
                print(f"{sub}: {mark}")
            return
    print("Student not found.")

def display_failed_students():
    print("\nStudents who failed in one or more subjects (marks < 40):")
    found = False
    for s in students:
        failed = [sub for sub, mark in s['marks'].items() if mark < 40]
        if failed:
            found = True
            print(f"{s['name']} (Roll: {s['roll']}) failed in: {', '.join(failed)}")
    if not found:
        print("No failures found.")

def update_marks():
    roll = input("Enter roll number to update marks: ")
    for s in students:
        if s['roll'] == roll:
            print("Enter new marks:")
            for sub in s['marks']:
                new_mark = int(input(f"{sub}: "))
                s['marks'][sub] = new_mark
            print("Marks updated successfully.")
            return
    print("Student not found.")

while True:
    print("\n--- Student Report Card Management System ---")
    print("1. Add New Student")
    print("2. View All Reports")
    print("3. Display Topper(s)")
    print("4. Search Student by Roll No.")
    print("5. Display Failed Students")
    print("6. Update Student Marks")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_all_reports()
    elif choice == '3':
        display_topper()
    elif choice == '4':
        search_by_roll()
    elif choice == '5':
        display_failed_students()
    elif choice == '6':
        update_marks()
    elif choice == '7':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
