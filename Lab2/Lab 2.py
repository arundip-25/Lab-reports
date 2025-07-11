n = int(input("Enter how many numbers: "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
