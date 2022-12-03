import re

lines = []

while True:
    line = input()

    if line:
        lines.append(line)
    else:
        break

text = '\n'.join(lines)

pattern = r'\d+'

numbers = re.findall(pattern, text)

print(' '.join(numbers))
