numbers = [int(number) for number in input().split(', ')]

step = 10
current_step = step

while len(numbers) > 0:
    current_list = [number for number in numbers if number <= current_step]
    numbers = [number for number in numbers if number not in current_list]
    print(f'Group of {current_step}\'s: {current_list}')
    current_step += step
