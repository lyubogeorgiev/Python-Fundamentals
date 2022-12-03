import re

pattern = r'^>>(\w+)<<(\d+\.?\d*)!(\d+)$'

furniture_bought = []
total_price = 0

while True:
    text = input()
    if text == 'Purchase':
        break

    current_matches = re.search(pattern, text)

    if current_matches:
        product = current_matches.groups()[0]
        price = float(current_matches.groups()[1])
        quantity = int(current_matches.groups()[2])

        furniture_bought.append(product)
        total_price += price * quantity

print('Bought furniture:')
[print(product) for product in furniture_bought]
print(f'Total money spend: {total_price:.2f}')



#         if product not in furniture_bought.keys():
#             furniture_bought[product] = [quantity, price]
#         else:
#             furniture_bought[product][0] += quantity
#             furniture_bought[product][1] = price
#
# total_price = 0
#
# for item in furniture_bought.values():
#     item_total_price = item[0] * item[1]
#     total_price += item_total_price
#
# print('Bought furniture:')
# [print(product) for product in furniture_bought.keys()]
# print(f'Total money spend: {total_price:.2f}')
