# Dictionary to store student names and their scores in 3 subjects
students = {
    "Bandhan": [85, 90, 78],
    "Deepak": [72, 88, 91],
    "Arundip": [90, 87, 93]
}

def display_averages(students):
    print("\nAverage marks of each student:")
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        print(f"{name}: {avg:.2f}")

def find_topper(students):
    topper = ""
    highest_avg = 0
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        if avg > highest_avg:
            highest_avg = avg
            topper = name
    print(f"\nTopper is {topper} with average marks of {highest_avg:.2f}")

def update_marks(students, name, new_marks):
    if name in students:
        students[name] = new_marks
        print(f"\nMarks updated for {name}.")
    else:
        print(f"\nStudent {name} not found.")

# Function calls
display_averages(students)
find_topper(students)

# Example of updating marks
update_marks(students, "Deepak", [80, 85, 88])
display_averages(students)
find_topper(students)
