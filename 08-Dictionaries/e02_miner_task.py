resourcesDictionary = {}

while True:
    firstLine = input()

    if firstLine == 'stop':
        break

    secondLine = int(input())

    if firstLine not in resourcesDictionary.keys():
        resourcesDictionary[firstLine] = 0

    resourcesDictionary[firstLine] += secondLine

[print(f'{key} -> {value}') for (key, value) in resourcesDictionary.items()]
