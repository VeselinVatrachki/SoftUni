products = {}
prices = "price"
quantities = "quantity"
command = input().split()

while command[0] != "buy":

    name, price, quantity = command[0], float(command[1]), int(command[2])

    products[name] = products.get(name, {})
    products[name][prices] = price
    products[name][quantities] = products[name].get(quantities, 0) + quantity

    command = input().split()

for product in products:
    total_price = products[product][prices] * products[product][quantities]
    print(f"{product} -> {total_price:.2f}")
