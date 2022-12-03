secret_message = input().split()
message = []

for word in secret_message:
    list_letters = [letter for letter in word]
    # print(list_letters)

    ascii_code = ''

    for letter in list_letters:
        # print(letter)
        if letter.isdigit():
            ascii_code += letter
            # print(list_letters)
            # list_letters.remove(letter)
            # print(list_letters)

    for digit in ascii_code:
        list_letters.remove(digit)

    first_letter = chr(int(ascii_code))

    list_letters.insert(0, first_letter)

    temp_letter = list_letters[1]
    list_letters[1] = list_letters[len(list_letters) - 1]
    list_letters[len(list_letters) - 1] = temp_letter

    # print(list_letters)

    message.append(''.join(list_letters))

print(' '.join(message))
