legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr',
                   'motes': "Dragonwrath"}

material_storage = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
legendary_item_obtained = ''

while True:
    user_input = input().split()

    for i in range(0, len(user_input), 2):
        quantity = int(user_input[i])
        item = user_input[i + 1].lower()

        if item in material_storage.keys():
            material_storage[item] += quantity

            if material_storage[item] >= 250:
                legendary_item_obtained = legendary_items[item]
                material_storage[item] -= 250
                break
        else:
            if item not in junk_materials.keys():
                junk_materials[item] = 0

            junk_materials[item] += quantity

    if legendary_item_obtained:
        break

print(f'{legendary_item_obtained} obtained!')
[print(f'{key}: {value}') for (key, value) in material_storage.items()]
[print(f'{key}: {value}') for (key, value) in junk_materials.items()]
