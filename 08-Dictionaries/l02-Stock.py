products = input().split()
productsAvailability = input().split()
productsCatalog = {}

for i in range(0, len(products), 2):
    productsCatalog[products[i]] = products[i + 1]

for searchedProduct in productsAvailability:
    if searchedProduct in productsCatalog.keys():
        print(f'We have {productsCatalog[searchedProduct]} of {searchedProduct} left')
    else:
        print(f'Sorry, we don\'t have {searchedProduct}')
