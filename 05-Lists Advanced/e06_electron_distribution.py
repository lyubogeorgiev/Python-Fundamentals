number_of_electrons = int(input())

electron_storage = []

while number_of_electrons > 0:
    position = len(electron_storage) + 1
    max_for_the_position = 2 * (position ** 2)
    if number_of_electrons <= max_for_the_position:
        electron_storage.append(number_of_electrons)
        break
    else:
        electron_storage.append(max_for_the_position)
        number_of_electrons -= max_for_the_position

print(electron_storage)
