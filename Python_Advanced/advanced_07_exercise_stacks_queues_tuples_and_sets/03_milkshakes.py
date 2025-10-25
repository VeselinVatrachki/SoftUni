from collections import deque


chocolates = [int(num) for num in input().split(", ")]
milk = deque([int(num) for num in input().split(", ")])
count = 0

while chocolates and milk and count < 5:
    if chocolates[-1] <= 0 and milk[0] <= 0:
        chocolates.pop()
        milk.popleft()
        continue

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue

    if milk[0] <= 0:
        milk.popleft()
        continue

    if chocolates[-1] == milk[0]:
        count += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolates[-1] -= 5

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join([str(n) for n in chocolates]) if chocolates else 'empty'}")
print(f"Milk: {', '.join([str(n) for n in milk]) if milk else 'empty'}")
