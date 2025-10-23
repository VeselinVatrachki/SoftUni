clothes = [int(x) for x in input().split()]
capacity = int(input())
racks = 0

while clothes:
    racks += 1
    current_rack_capacity = capacity
    while clothes and clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes.pop()

print(racks)
