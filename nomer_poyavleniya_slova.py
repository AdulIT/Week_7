fin = open('input.txt')
letters = dict()
for line in fin:
    newFile = line.split()
    for i in newFile:
        letters[i] = letters.get(i, -1) + 1
        print(letters[i], end=' ')
