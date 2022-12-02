a = []
b = []

[a.append(player) for player in range(1, 12)]
[b.append(player) for player in range(1, 12)]

isTerminated = False

cards = input().split()
for card in cards:
    card_tokens = card.split('-')

    team = card_tokens[0].lower()
    player_number = int(card_tokens[1])

    if team == 'a':
        if player_number not in a:
            continue
        a.remove(player_number)
    else:
        if player_number not in b:
            continue
        b.remove(player_number)

    if len(a) < 7 or len(b) < 7:
        isTerminated = True
        break

print(f'Team A - {len(a)}; ', end='')
print(f'Team B - {len(b)}')

if isTerminated:
    print('Game was terminated')
