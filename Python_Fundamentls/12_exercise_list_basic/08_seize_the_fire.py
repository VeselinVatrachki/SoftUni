fire_level = input().split("#")
water = int(input())

extinguish_cells = []
effort = 0
total_fire = 0
water_left = water

for text in fire_level:
    fire_data = text.split(" =")
    fire_type = fire_data[0]
    cell_value = int(fire_data[1])
    if water_left >= cell_value:
        if fire_type == "High" and 81 <= cell_value <= 126:
            extinguish_cells.append(cell_value)
            effort += cell_value * 0.25
            total_fire += cell_value
            water_left -= cell_value
        elif fire_type == "Medium" and 51 <= cell_value < 81:
            extinguish_cells.append(cell_value)
            effort += cell_value * 0.25
            total_fire += cell_value
            water_left -= cell_value
        elif fire_type == "Low" and 1 <= cell_value < 51:
            extinguish_cells.append(cell_value)
            effort += cell_value * 0.25
            total_fire += cell_value
            water_left -= cell_value

print("Cells:")
for cell in extinguish_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
