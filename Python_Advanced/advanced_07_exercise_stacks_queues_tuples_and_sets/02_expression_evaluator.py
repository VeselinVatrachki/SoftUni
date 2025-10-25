from collections import deque


user_input = input().split()
queue = deque()

def calculate(a:int, b:int, operator:str)->int:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b


for char in user_input:
    if char not in "+-*/":
        queue.append(int(char))
    else:
        while len(queue) > 1:
            num_1 = queue.popleft()
            num_2 = queue.popleft()
            calculate(num_1, num_2, char)

print(queue.popleft())
