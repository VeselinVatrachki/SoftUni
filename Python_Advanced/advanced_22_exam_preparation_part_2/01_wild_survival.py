from collections import deque


bees = deque(int(num) for num in input().split())
eaters = [int(num) for num in input().split()]
bees_killed_by_bee_eater = 7

while bees and eaters:
    current_bees = bees.popleft()
    current_eaters = eaters.pop()

    while current_bees > 0 and current_eaters > 0:
        current_bees -= bees_killed_by_bee_eater
        if current_bees >= 0:
           current_eaters -= 1

    if current_bees > 0:
        bees.append(current_bees)
    elif current_eaters > 0:
        eaters.append(current_eaters)

print("The final battle is over!")
if bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
elif eaters:
    print(f"Bee-eater groups left: {', '.join(map(str, eaters))}")
else:
    print("But no one made it out alive!")
