number = int(input())

all_numbers_even = True

for i in range(number):
    current_number = int(input())

    if not current_number % 2 == 0:
        print(f'{current_number} is odd!')
        all_numbers_even = False
        break

if all_numbers_even:
    print("All numbers are even.")
