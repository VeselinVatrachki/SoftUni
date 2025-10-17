some_string = input().split()
search_items = input().split()
bakery = {}

for i in range(0, len(some_string), 2):
    key = some_string[i]
    value = some_string[i+1]
    bakery[key] = int(value)

for item in search_items:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
