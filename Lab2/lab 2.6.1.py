n = int(input("Enter number of elements: "))
nums = []

for _ in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

numbers = tuple(nums)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers = list(numbers)
            numbers[i] = numbers[j]
            numbers[j] = temp
            numbers = tuple(numbers)

if len(numbers) % 2 == 1:
    median = numbers[len(numbers) // 2]
else:
    mid1 = numbers[len(numbers) // 2 - 1]
    mid2 = numbers[len(numbers) // 2]
    median = (mid1 + mid2) / 2

print("Median:", median)
