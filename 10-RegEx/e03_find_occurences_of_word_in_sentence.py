import re

text = input()
word = input()

occurrences = re.findall(rf'\b{word}\b', text, re.IGNORECASE)

# print(occurrences)
print(len(occurrences))
