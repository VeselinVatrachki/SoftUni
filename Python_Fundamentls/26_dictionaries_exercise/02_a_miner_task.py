resource = input()
result = {}

while resource != 'stop':

    quantity = int(input())
    result[resource] = result.get(resource, 0) + quantity

    resource = input()

for resource, quantity in result.items():
    print(f'{resource} -> {quantity}')
