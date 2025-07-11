n = int(input("Enter number of elements: "))
nums = []

for _ in range(n):
    num = float(input("Enter number: "))
    nums.append(num)

numbers = tuple(nums)
unique = []
counts = []

for num in numbers:
    if num not in unique:
        unique.append(num)
        counts.append(1)
    else:
        idx = unique.index(num)
        counts[idx] += 1

max_count = counts[0]
mode = unique[0]

for i in range(1, len(counts)):
    if counts[i] > max_count:
        max_count = counts[i]
        mode = unique[i]

print("Mode:", mode)
