def is_palindrome(number_to_check):
    number_to_check_len = len(number_to_check)
    for i in range(0, number_to_check_len // 2):
        if number_to_check[i] != number_to_check[number_to_check_len - i - 1]:
            return False

    return True


numbers = input().split(', ')

result = [str(is_palindrome(number)) for number in numbers]
print('\n'.join(result))
