text = input()

result = ''.join([chr(ord(ch) + 3) for ch in text])

print(result)
