n = int(input())

chair_balance = 0
is_all_set = True

for i in range(n):
    input_tokens = input().split()

    chairs = len(input_tokens[0])
    guests = int(input_tokens[1])

    if chairs >= guests:
        chair_balance += (chairs - guests)
    else:
        is_all_set = False
        print(f'{guests - chairs} more chairs needed in room {i + 1}')

if is_all_set:
    print(f'Game On, {chair_balance} free chairs left')
