number_of_commands = int(input())
parking_cars = set()

for _ in range(number_of_commands):
    command, car_plate = input().split(", ")
    if command == "IN":
        parking_cars.add(car_plate)
    elif command == "OUT":
        parking_cars.remove(car_plate)

if parking_cars:
    print(*parking_cars, sep="\n")
else:
    print("Parking Lot is Empty")
