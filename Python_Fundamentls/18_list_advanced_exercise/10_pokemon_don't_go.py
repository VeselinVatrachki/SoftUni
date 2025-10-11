distance_to_the_pokemon = [int(num) for num in input().split()]

results = []

while distance_to_the_pokemon:
    position = int(input())
    captured_pokemon = ""

    if position < 0:
        captured_pokemon = distance_to_the_pokemon.pop(0)
        distance_to_the_pokemon.insert(0, distance_to_the_pokemon[-1])
    elif position >= len(distance_to_the_pokemon):
        captured_pokemon = distance_to_the_pokemon.pop(-1)
        distance_to_the_pokemon.append(distance_to_the_pokemon[0])
    if not captured_pokemon:
        captured_pokemon = distance_to_the_pokemon.pop(position)
    results.append(captured_pokemon)

    for i, pokemon in enumerate(distance_to_the_pokemon):
        if pokemon <= captured_pokemon:
            distance_to_the_pokemon[i] += captured_pokemon
        else:
            distance_to_the_pokemon[i] -= captured_pokemon

print(sum(results))
