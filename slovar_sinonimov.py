n = int(input())
myDict = {}
for i in range(n):
    word, sameWord = input().split()
    myDict[word] = sameWord
    myDict[sameWord] = word
slovo = input()
print(myDict[slovo])
