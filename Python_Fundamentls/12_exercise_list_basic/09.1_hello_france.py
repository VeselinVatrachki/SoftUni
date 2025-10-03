ticket_price = 150
collection_of_items = input().split("|")
budget = float(input())
budget_left = budget
profit = 0
sell_price = []
total_profit = 0

for items in collection_of_items:
    item = items.split("->")
    type_of_item, price_of_item = item[0], float(item[1])

    if budget_left >= price_of_item:

        if type_of_item == "Clothes" and price_of_item <= 50:
            budget_left -= price_of_item
            clothes = round(price_of_item * 1.40, 2)
            profit += (clothes - price_of_item)
            sell_price.append(str(clothes))

        elif type_of_item == "Shoes" and price_of_item <= 35:
            budget_left -= price_of_item
            shoes = round(price_of_item * 1.40, 2)
            profit += (shoes - price_of_item)
            sell_price.append(str(shoes))

        elif type_of_item == "Accessories" and price_of_item <= 20.50:
            budget_left -= price_of_item
            accessories = round(price_of_item * 1.40, 2)
            profit += (accessories - price_of_item)
            sell_price.append(str(accessories))
