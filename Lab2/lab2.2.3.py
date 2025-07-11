n = int(input("Enter how many numbers: "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)
