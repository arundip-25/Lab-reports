all_students = set(input("Enter roll numbers of all students (space-separated): ").split())
football = set(input("Enter roll numbers of football players (space-separated): ").split())
cricket = set(input("Enter roll numbers of cricket players (space-separated): ").split())

both = football & cricket
only_one = football ^ cricket
neither = all_students - (football | cricket)

print("Students who play both sports:", both)
print("Students who play only one sport:", only_one)
print("Students who play neither sport:", neither)
