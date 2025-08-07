number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_caps = float(input())
    days = int(input())
    caps_per_day = int(input())
    if price_per_caps < 0.01 or price_per_caps > 100.00:
        continue
    elif days < 1 or days > 31:  # days not in range(1, 31+1)
        continue
    elif caps_per_day < 1 or caps_per_day > 2000:  # caps_per_day not in range(1, 2000+1)
        continue
    price = price_per_caps * days * caps_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
