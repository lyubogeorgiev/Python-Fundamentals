numbers = input().split(', ')
count = int(input())

result = list()

for i in range(count):
    numbersSum = 0
    for j in range(i, len(numbers), count):
        numbersSum += int(numbers[j])

    result.append(numbersSum)

print(result)
