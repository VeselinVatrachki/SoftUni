vehicles = input().split(">>")
family_car_tax = 50
heavyDuty_car_tax = 80
sports_car_tax = 100
total_tax = 0
for car in vehicles:
    car_type = car.split(" ")[0]
    years_for_tax = int(car.split(" ")[1])
    kilometers = int(car.split(" ")[2])
    if car_type == "family":
        tax_increase = (kilometers // 3000) * 12
        tax_declines = 5 * years_for_tax
        tax = tax_increase + (family_car_tax - tax_declines)
        total_tax += tax
    elif car_type == "heavyDuty":
        tax_increase = (kilometers // 9000) * 14
        tax_declines = 8 * years_for_tax
        tax = tax_increase + (heavyDuty_car_tax - tax_declines)
        total_tax += tax
    elif car_type == "sports":
        tax_increase = (kilometers // 2000) * 18
        tax_declines = 9 * years_for_tax
        tax = tax_increase + (sports_car_tax - tax_declines)
        total_tax += tax
    else:
        print("Invalid car type.")
        continue
    print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
