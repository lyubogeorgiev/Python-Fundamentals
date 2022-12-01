count = int(input())

synonymDictionary = {}

for i in range(count):
    word = input()
    synonym = input()

    if word not in synonymDictionary.keys():
        synonymDictionary[word] = []

    synonymDictionary[word].append(synonym)

for (key, value) in synonymDictionary.items():
    print(f'{key} - {", ".join(value)}')
