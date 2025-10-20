import re
pattern_name = r'([A-Za-z]+)'
pattern_distance = r'([\d+])'
participants = input().split(", ")
while True:
    command = input()
    if command == 'end of race':
        break

    name = "".join(re.findall(pattern_name, command))
    distances = "".join(re.findall(pattern_distance, command))
    distance = sum(int(num) for num in distances)
    if name in participants:
        participants[name] = {'distance': distance}
        print(f"{name} has {distance} points")

