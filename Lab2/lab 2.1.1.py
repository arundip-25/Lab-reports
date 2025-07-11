n = int(input("Enter how many numbers: "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)
