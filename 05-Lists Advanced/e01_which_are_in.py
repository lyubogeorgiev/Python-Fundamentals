list_one = input().split(', ')
list_two = input().split(', ')

result = []

for word in list_one:
    for full_word in list_two:
        if word in full_word:
            result.append(word)
            break

print(result)
