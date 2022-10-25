command = input()

while not command == "End":
    if not command == "SoftUni":
        result_list = []

        for letter in command:
            result_list.append(letter * 2)

        print(''.join(result_list))

    command = input()
    