budget = int(input())
command = input()

while command != "End":
    price = int(command)
    total_price += price

    if total_price > budget:
        print("You went in overdraft!")
        break
