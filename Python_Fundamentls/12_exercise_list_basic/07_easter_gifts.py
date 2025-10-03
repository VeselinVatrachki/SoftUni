gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    tokens = command.split()

    if tokens[0] == 'OutOfStock':
        for index, value in enumerate(gifts):
            if value == tokens[1]:
                change = "None"
                gifts.pop(index)
                gifts.insert(index, change)
    elif tokens[0] == 'Required':
        if len(gifts) - 1 > int(tokens[2]) >= 0:
            index = int(tokens[2])
            gifts[index] = tokens[1]
    elif tokens[0] == 'JustInCase':
        gifts[-1] = tokens[1]

result = [gift for gift in gifts if gift != "None"]
print(" ".join(result))
