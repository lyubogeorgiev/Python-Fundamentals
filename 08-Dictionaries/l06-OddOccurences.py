userInput = input().split(' ')

words = {}

for word in userInput:
    lowerWord = word.lower()
    if lowerWord not in words.keys():
        words[lowerWord] = 0

    words[lowerWord] += 1

resultDict = []

for (key, value) in words.items():
    if value % 2 != 0:
        resultDict.append(key)

print(' '.join(resultDict))
