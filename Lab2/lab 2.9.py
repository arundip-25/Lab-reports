import random
num=int(input("Numbers that are wanted to be included: "))

numbers = set()

while len(numbers) < 10:
    num = random.randint(1, 100)
    numbers.add(num)

print("Original set with 10 unique elements:", numbers)

min_val = min(numbers)
max_val = max(numbers)

numbers.remove(min_val)
numbers.remove(max_val)

print("Set after removing smallest and largest elements:")
print(numbers)

