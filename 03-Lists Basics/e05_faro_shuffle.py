cards = input().split()
n = int(input())

for i in range(n):
    deck_one = cards[:len(cards) // 2]
    deck_two = cards[len(cards) // 2:]
    cards.clear()

    for j in range(len(deck_one)):
        cards.append(deck_one[j])
        cards.append(deck_two[j])

print(cards)
