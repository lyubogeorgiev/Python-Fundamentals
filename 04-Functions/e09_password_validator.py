def is_between_6_and_10_chars(password):
    if 6 <= len(password) <= 10:
        return True

    return False


def is_only_letters_and_digits(password):
    if password.isalnum():
        return True

    return False


def has_at_least_two_digits(password):
    digits = list(filter(lambda d: d.isdigit(), password))

    if len(digits) >= 2:
        return True

    return False


def password_validator(password):
    is_valid = True
    if not is_between_6_and_10_chars(password):
        is_valid = False
        print('Password must be between 6 and 10 characters')

    if not is_only_letters_and_digits(password):
        is_valid = False
        print('Password must consist only of letters and digits')

    if not has_at_least_two_digits(password):
        is_valid = False
        print('Password must have at least 2 digits')

    if is_valid:
        print('Password is valid')


user_input = input()

password_validator(user_input)
