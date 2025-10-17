some_string = input().split()
bakery = {}

for i in range(0, len(some_string), 2):
    key = some_string[i]
    value = some_string[i+1]
    bakery[key] = int(value)

print(bakery)