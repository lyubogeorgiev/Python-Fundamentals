userInput = input().replace(' ', '')

charsDictionary = {}

for char in userInput:
    if char not in charsDictionary.keys():
        charsDictionary[char] = 0

    charsDictionary[char] += 1

[print(f'{key} -> {value}') for (key, value) in charsDictionary.items()]
