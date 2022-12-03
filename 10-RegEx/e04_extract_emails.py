import re

text = input()

# print(text)

# pattern = r"[._0-9A-Za-z]+@\w+\.\w+(\.\w+)*(?=\s|$)"
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern = r'(?<=[\s^])[A-Za-z0-9][A-Za-z0-9._%+-]+@[a-zA-Z0-9][A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails = re.findall(pattern, text, re.MULTILINE)

print('\n'.join(emails))

