text = input()
i = 0

while True:
    if i >= len(text) - 1:
        break

    if text[i] == text[i + 1]:
        text = text[:i + 1] + text[i + 2:]
    else:
        i += 1

print(text)
