phonebook = {}

user_input = input()

while not user_input.isnumeric():
    current_contact = user_input.split('-')

    name = current_contact[0]
    phone_number = current_contact[1]

    if name not in phonebook.keys():
        phonebook[name] = ''

    phonebook[name] = phone_number

    user_input = input()

numberOfContacts = int(user_input)

for i in range(numberOfContacts):
    user_input = input()

    if user_input in phonebook.keys():
        print(f'{user_input} -> {phonebook[user_input]}')
    else:
        print(f'Contact {user_input} does not exist.')
        