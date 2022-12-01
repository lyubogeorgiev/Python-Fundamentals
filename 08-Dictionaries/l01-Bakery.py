userInput = input().split(' ')

# print(userInput)

products = {}

for i in range(0, len(userInput), 2):
    key = userInput[i]
    value = int(userInput[i + 1])

    products[key] = value
    # print(f'{userInput[i]}: {userInput[i + 1]}')

print(products)