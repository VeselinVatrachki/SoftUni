import re
bought_furniture = []
command = input()
total_cost = 0
pattern = r'>>([A-Za-z]+)<<([0-9\.]+)!([0-9]+)'  # >>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)
while command != 'Purchase':
    match = re.search(pattern, command)
    if match:
        furniture = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))
        bought_furniture.append(furniture)
        total_cost += price * quantity

    command = input()

print(f"Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f'Total money spend: {total_cost:.2f}')