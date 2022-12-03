numbers = [int(number) for number in input().split(', ')]
even = list()
odd = list()

positive = [number for number in numbers if number >= 0]
negative = [number for number in numbers if number < 0]
[even.append(number) for number in numbers if number % 2 == 0]
[odd.append(number) for number in numbers if number % 2 != 0]

# print(f'Positive: {", ".join(positive)}')
print(f"Positive: {', '.join([str(number) for number in positive])}")
print(f"Negative: {', '.join([str(number) for number in negative])}")
print(f"Even: {', '.join([str(number) for number in even])}")
print(f"Odd: {', '.join([str(number) for number in odd])}")
