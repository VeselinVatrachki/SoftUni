from collections import deque


green_light_duration = int(input())
window = int(input())
cars = deque()
count_cars = 0
car_crashed = False

while True:
    command = input()
    if command == 'END':
        break

    if command == 'green':
        if cars:
            curr_car = cars.popleft()
            remaining_green = green_light_duration - len(curr_car)

            while remaining_green > 0:
                count_cars += 1
                if not cars:
                    break
                curr_car = cars.popleft()
                remaining_green -= len(curr_car)

            if remaining_green == 0:
                count_cars += 1

            if window >= abs(remaining_green):
                if remaining_green < 0:
                    count_cars += 1
            else:
                index = window + remaining_green
                print(f"A crash happened!\n{curr_car} was hit at {curr_car[index]}.")
                car_crashed = True
                break

    else:
        cars.append(command)

if not car_crashed:
    print(f"Everyone is safe.\n{count_cars} total cars passed the crossroads.")
