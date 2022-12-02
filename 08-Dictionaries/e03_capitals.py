countries = input().split(', ')
cities = input().split(', ')

[print(f'{key} -> {value}') for (key, value) in zip(countries, cities)]
