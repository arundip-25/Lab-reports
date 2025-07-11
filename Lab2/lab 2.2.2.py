n = int(input("Enter how many numbers: "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted list in ascending order:", numbers)
