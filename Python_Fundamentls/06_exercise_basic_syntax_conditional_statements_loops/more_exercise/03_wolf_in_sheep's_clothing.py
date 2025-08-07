sheep_list = input().split(", ")

if sheep_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    sheep_position = len(sheep_list) - sheep_list.index("wolf") - 1
    print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")
    