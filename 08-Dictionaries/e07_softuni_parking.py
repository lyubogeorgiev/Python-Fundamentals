num = int(input())

garage = {}

for i in range(num):
    user_input = input().split()

    command = user_input[0]
    name = user_input[1]

    if command == 'register':
        license_plate = user_input[2]
        if name not in garage.keys():
            garage[name] = license_plate

            print(f'{name} registered {garage[name]} successfully')
        else:
            print(f'ERROR: already registered with plate number {garage[name]}')
    else:
        if name not in garage.keys():
            print(f'ERROR: user {name} not found')
        else:
            garage.pop(name)
            print(f'{name} unregistered successfully')

[print(f'{key} => {value}') for (key, value) in garage.items()]
