version = [int(number) for number in input().split('.')]

ones = version[2] + 1
tens = version[1]
hundreds = version[0]

if ones > 9:
    ones = 0
    tens += 1

    if tens > 9:
        tens = 0
        hundreds += 1

print(f'{hundreds}.{tens}.{ones}')
