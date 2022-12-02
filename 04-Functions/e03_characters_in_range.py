def characters_in_range(first_char, second_char):
    return ' '.join([chr(code) for code in range(ord(first_char) + 1, ord(second_char))])


char_one = input()
char_two = input()

print(characters_in_range(char_one, char_two))
