from collections import deque

boxes = [int(num) for num in input().split()]
magic = deque([int(num) for num in input().split()])
presents = {}
items = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while magic and boxes:
    current_magic = magic[0] * boxes[-1]
    if current_magic in items:
        current_present = items[current_magic]
        if current_present not in presents:
            presents[current_present] = 0
        presents[current_present] += 1
        boxes.pop()
        magic.popleft()
    elif current_magic < 0:
        boxes.append(magic.popleft() + boxes.pop())
    elif current_magic > 0:
        magic.popleft()
        boxes[-1] += 15
    else:
        if boxes[-1] == 0: boxes.pop()
        if magic[0] == 0: magic.popleft()

if ("Doll" in presents) and ("Wooden train" in presents) \
    or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join([str(x) for x in boxes[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")
for key, value in sorted(presents.items()):
    print(f"{key}: {value}")
