class Party:

    def __init__(self):
        self.people = []


user_input = input()
party = Party()

while not user_input == "End":
    party.people.append(user_input)

    user_input = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
