n = int(input("Enter number of elements: "))
nums = []

for _ in range(n):
    num = int(input("Enter number: "))
    nums.append(num)

numbers = tuple(nums)
total = 0

for val in numbers:
    total += val

average = total / len(numbers)
print("Average:", average)
