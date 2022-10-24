budget = int(input())

user_input = ''

while budget >= 0 and not user_input.lower() == "end":
    user_input = input()
    if  user_input.lower() == "end":
        break
    price = int(user_input)
    budget -= price

if budget >= 0:
    print('You bought everything needed.')
else:
    print('You went in overdraft!')
