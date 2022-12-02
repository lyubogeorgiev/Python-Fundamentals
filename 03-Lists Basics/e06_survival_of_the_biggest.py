numbers = input().split()
count = int(input())

numbers = [int(number) for number in numbers]

for i in range(count):
    smallest_number = min(numbers)
    numbers.remove(smallest_number)

print(', '.join([str(number) for number in numbers]))
