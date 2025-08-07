budget = float(input())
flour_price_per_kg = float(input())

egg_pack_price = flour_price_per_kg * 0.75
milk_price_per_litre = flour_price_per_kg * 1.25
number_of_bread = 0
colored_eggs = 0
total_price = 0
bread_price = egg_pack_price + flour_price_per_kg + (milk_price_per_litre / 4)

while True:
    total_price += bread_price
    if total_price > budget:
        total_price -= bread_price
        break
    number_of_bread += 1
    colored_eggs += 3
    if number_of_bread % 3 == 0:
        colored_eggs -= (number_of_bread - 2)

money_left = budget - total_price

print(f"You made {number_of_bread} loaves of Easter bread!\
 Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
