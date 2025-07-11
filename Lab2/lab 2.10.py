def unique_vowels(sentence):
    vowels = "aeiouAEIOU"
    result = set()
    for char in sentence:
        if char in vowels:
            result.add(char.lower())
    return result

# Example usage
text = input("Enter a sentence: ")
print("Unique vowels used:", unique_vowels(text))
