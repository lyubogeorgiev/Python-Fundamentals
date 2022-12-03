def is_right_length(word):
    if 3 <= len(word) <= 16:
        return True

    return False


def contains_right_symbols(word):
    for symbol in word:
        if not (symbol.isalnum() or symbol == '-' or symbol == '_'):
            return False

    return True


def no_redundant_symbols(word):
    if ' ' in word:
        return False

    return True


def is_valid(word):
    if is_right_length(word) and contains_right_symbols(word) and no_redundant_symbols(word):
        return True

    return False


user_input = input().split(', ')

for word in user_input:
    if is_valid(word):
        print(word)
