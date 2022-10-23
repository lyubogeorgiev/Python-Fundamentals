coffee_list = input().split(" ")
n = int(input())

for i in range(n):
    command = input()
    command_tokens = command.split(" ")

    if command_tokens[0] == "Include":
        coffee_list.append(command_tokens[1])

    elif command_tokens[0] == "Remove":
        if command_tokens[1] == "first":
            if int(command_tokens[2]) > len(coffee_list):
                continue
            else:
                coffee_list = coffee_list[int(command_tokens[2]):]

        elif command_tokens[1] == "last":
            if int(command_tokens[2]) > len(coffee_list):
                continue
            else:
                coffee_list = coffee_list[:len(coffee_list) - int(command_tokens[2])]

    elif command_tokens[0] == "Prefer":
        first_coffee_index = int(command_tokens[1])
        second_coffee_index = int(command_tokens[2])

        if first_coffee_index >= len(coffee_list) or second_coffee_index >= len(coffee_list):
            continue
        else:
            coffee_list[first_coffee_index], coffee_list[second_coffee_index] = \
                coffee_list[second_coffee_index], coffee_list[first_coffee_index]

    elif command_tokens[0] == "Reverse":
        coffee_list.reverse()

coffee_list_string = ' '.join(coffee_list)
print("Coffees:")
print(f'{coffee_list_string}')
