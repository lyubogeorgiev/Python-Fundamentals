userInput = input().split(': ')
statistics = {}

while len(userInput) > 1:
    product = userInput[0]
    quantity = int(userInput[1])

    if product not in statistics:
        statistics[product] = 0

    statistics[product] += quantity
    userInput = input().split(': ')

print('Products in stock:')
for key, value in statistics.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(statistics)}')
print(f'Total Quantity: {sum(statistics.values())}')
