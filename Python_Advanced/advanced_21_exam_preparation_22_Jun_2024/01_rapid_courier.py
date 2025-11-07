from collections import deque


packages = [int(el) for el in input().split()]
couriers = deque([int(el) for el in input().split()])

total_delivered_weight = 0

while packages and couriers:
    curr_package = packages[-1]
    curr_courier = couriers[0]

    if curr_courier >= curr_package:
        capacity = curr_courier - curr_package * 2
        couriers.popleft()
        if capacity > 0:
            couriers.append(capacity)
        total_delivered_weight += packages.pop()
    else:
        packages[-1] -= couriers.popleft()
        total_delivered_weight += curr_courier

print(f"Total weight: {total_delivered_weight} kg")

if not packages and not couriers:
    print(f"Congratulations, all packages were delivered successfully by the couriers today.")

if packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")

if couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")