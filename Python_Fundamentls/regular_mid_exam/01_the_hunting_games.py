days = int(input())
players = int(input())
group_energy = float(input())
daily_water_per_person = float(input())
daily_food_per_person = float(input())
total_water = float(days * daily_water_per_person * players)
total_food = float(days * daily_food_per_person * players)
count_days = 0
for day in range(days):
    daily_energy = float(input())
    group_energy -= daily_energy
    count_days += 1
    if group_energy <= 0:
        break

    if count_days % 2 == 0:
        total_water -= total_water * 0.3
        group_energy += group_energy * 0.05

    if count_days % 3 == 0:
        total_food -= total_food / players
        group_energy += group_energy * 0.1

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
