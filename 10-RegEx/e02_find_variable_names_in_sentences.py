import re

text = input()

pattern = r'(?<=\s_)[a-zA-Z0-9]+(?=\s|$)'

variables = re.findall(pattern, text)

print(','.join(variables))
