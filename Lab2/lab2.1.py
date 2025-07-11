n = int(input("Enter how many numbers: "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()
print("Sorted list in ascending order:", numbers)
