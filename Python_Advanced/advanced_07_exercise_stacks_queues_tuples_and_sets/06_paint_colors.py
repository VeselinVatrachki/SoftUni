from collections import deque


string = deque(input().split())
main_colors = ["red", "blue", "yellow", "orange", "purple", "green"]
result = []


def check_color(color, array):
    if color == "orange" and "red" in array and "yellow" in array:
        return True
    elif color == "purple" and "blue" in array and "red" in array:
        return True
    elif color == "green" and "blue" in array and "yellow" in array:
        return True
    elif color == "red" or color == "blue" or color == "yellow":
        return True
    else:
        return False


while string:
    first = string.popleft()
    last = string.pop() if string else ''
    for color in (first + last, last + first):
        if color in main_colors:
            result.append(color)
            break
    else:
        if len(first) > 1:
            string.insert(len(string) // 2, first[:-1])
        if len(last) > 1:
            string.insert(len(string) // 2, last[:-1])

for color in result:
    if not check_color(color, result):
        result.remove(color)

print(result)
