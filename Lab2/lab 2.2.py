n1 = int(input("Enter number of elements in first list: "))
list1 = []
for _ in range(n1):
    list1.append(int(input("Enter number: ")))

n2 = int(input("Enter number of elements in second list: "))
list2 = []
for _ in range(n2):
    list2.append(int(input("Enter number: ")))

merged = list1 + list2

common = []
for item in list1:
    if item in list2 and item not in common:
        common.append(item)

result = []
for item in merged:
    if item not in common:
        result.append(item)

print("Merged list without common elements:", result)
