products = {}

while True:
    user_input = input()
    if user_input == 'buy':
        break

    product = user_input.split()

    name = product[0]
    productPrice = float(product[1])
    productQuantity = int(product[2])

    if name not in products.keys():
        products[name] = {'price': 0.0, 'quantity': 0}
        # products[name]['price'] = 0.0
        # products[name]['quantity'] = 0

    products[name]['price'] = productPrice
    products[name]['quantity'] += productQuantity

[print(f'{key} -> {(value["price"] * value["quantity"]):.2f}') for (key, value) in products.items()]
