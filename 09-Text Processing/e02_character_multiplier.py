user_input = input().split()

first_string = user_input[0]
second_string = user_input[1]

longer_string = second_string
shorter_string = first_string

strings_sum = 0

if len(first_string) > len(second_string):
    longer_string = first_string
    shorter_string = second_string

for i in range(len(longer_string)):
    if i < len(shorter_string):
        strings_sum += (ord(longer_string[i]) * ord(shorter_string[i]))
    else:
        strings_sum += ord(longer_string[i])

print(strings_sum)
