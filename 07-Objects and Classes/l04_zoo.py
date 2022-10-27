class Zoo:

    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        current_species_list = []
        species_name = ''

        if species == 'mammal':
            current_species_list = self.mammals
            species_name = 'Mammals'
        elif species == 'fish':
            current_species_list = self.fishes
            species_name = 'Fishes'
        elif species == 'bird':
            current_species_list = self.birds
            species_name = 'Birds'

        total_animals_in_zoo = len(self.mammals) + len(self.birds) + len(self.fishes)

        return f'{species_name} in {self.zoo_name}: {", ".join(current_species_list)}' \
               f'\nTotal animals: {total_animals_in_zoo}'


zoo_name_input = input()
number_of_inputs = int(input())

current_zoo = Zoo(zoo_name_input)

for i in range(number_of_inputs):
    user_input = input().split(' ')

    current_zoo.add_animal(user_input[0], user_input[1])

print(current_zoo.get_info(input()))
