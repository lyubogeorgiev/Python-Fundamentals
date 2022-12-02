def is_it_perfect_number(number):
    digits = []
    number_int = int(number)

    for i in range(1, (number_int // 2) + 1):
        if number_int % i == 0:
            digits.append(i)

    if sum(digits) == number_int:
        return 'We have a perfect number!'

    return 'It\'s not so perfect.'


user_input = input()

print(is_it_perfect_number(user_input))
