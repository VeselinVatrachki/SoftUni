materials = {"shards": 0, "fragments": 0, "motes": 0}
won_legendary_item = False

while not won_legendary_item:
    current_items = input().split()

    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()

        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value

        if materials["shards"] >= 250:
            materials["shards"] -= 250
            print("Shadowmourne obtained!")
            won_legendary_item = True

        elif materials["fragments"] >= 250:
            materials["fragments"] -= 250
            print("Valanyr obtained!")
            won_legendary_item = True

        elif materials["motes"] >= 250:
            materials["motes"] -= 250
            print("Dragonwrath obtained!")
            won_legendary_item = True

        if won_legendary_item:
            break

for material, quantity in materials.items():
    print(f"{material}: {quantity}")
