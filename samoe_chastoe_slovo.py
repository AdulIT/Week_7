fin = open('input.txt', encoding='utf8')
dictionary = {}
for line in fin:
    words = line.strip().split()
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
print(sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))[0][0])
