sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = []
counts = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)
        counts.append(1)
    else:
        index = unique_words.index(word)
        counts[index] += 1

for i in range(len(unique_words)):
    print(unique_words[i], ":", counts[i])
