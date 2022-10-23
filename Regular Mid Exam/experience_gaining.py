needed_experience = float(input())
count_of_battles = int(input())
# experience_earned_per_battle = float(input())

current_experience = 0
current_battle = 0

while current_experience < needed_experience and current_battle < count_of_battles:
    current_battle += 1
    # current_experience += float(input())
    experience_gained = float(input())

    if current_battle % 3 == 0:
        experience_gained += experience_gained * 0.15
    elif current_battle % 5 == 0:
        experience_gained -= experience_gained * 0.1
    elif current_battle % 10 == 0:
        experience_gained += experience_gained * 0.05

    current_experience += experience_gained

if current_experience >= needed_experience:
    print(f'Player successfully collected his needed experience for {current_battle} battles.')
else:
    print(f'Player was not able to collect the needed experience, {abs(current_experience -needed_experience):.2f} more '
          f'needed.')
