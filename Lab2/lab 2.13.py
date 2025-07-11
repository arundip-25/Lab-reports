text = input("Enter a text: ")
frequency = {}

for char in text:
    if char.isalnum():  # checks if character is a letter or digit
        char = char.lower()
        frequency[char] = frequency.get(char, 0) + 1

print("Character frequency:")
for char, count in frequency.items():
    print(f"{char}: {count}")
