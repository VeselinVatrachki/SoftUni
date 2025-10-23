from collections import deque

expression = deque(input())
open_parentheses = '([{'
close_parentheses = ')]}'
counter = 0

while expression and counter < len(expression) / 2:
    if expression[0] not in open_parentheses:
        break

    index = open_parentheses.index(expression[0])
    if expression[1] == close_parentheses[index]:
        expression.popleft()
        expression.popleft()
        expression.rotate(counter)
        counter = 0
    else:
        expression.rotate(-1)
        counter += 1

if expression:
    print("NO")
else:
    print("YES")