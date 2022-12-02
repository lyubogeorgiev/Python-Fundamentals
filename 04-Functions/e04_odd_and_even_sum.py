number = input()


def odd_and_even_sum(digits):
    even_sum = 0
    odd_sum = 0

    for digit in digits:
        digit_int = int(digit)
        if digit_int % 2 == 0:
            even_sum += digit_int
        else:
            odd_sum += digit_int

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(odd_and_even_sum(number))
