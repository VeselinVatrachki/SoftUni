from math import floor


def longer_line(x, y, a, b):
    dist_1 = x + y
    dist_2 = a + b
    if dist_1 > dist_2:
        if x > y:
            return f"({y_1}, {y_2})({x_1}, {x_2})"
        else:
            return f"({x_1}, {x_2})({y_1}, {y_2})"
    elif dist_1 < dist_2:
        if a > b:
            return f"({b_1}, {b_2})({a_1}, {a_2})"
        else:
            return f"({a_1}, {a_2})({b_1}, {b_2})"
    else:
        if a > b:
            return f"({b_1}, {b_2})({a_1}, {a_2})"
        else:
            return f"({a_1}, {a_2})({b_1}, {b_2})"


x_1, x_2 = floor(float(input())), floor(float(input()))
y_1, y_2 = floor(float(input())), floor(float(input()))
a_1, a_2 = floor(float(input())), floor(float(input()))
b_1, b_2 = floor(float(input())), floor(float(input()))

x = abs(x_1) + abs(x_2)
y = abs(y_1) + abs(y_2)
a = abs(a_1) + abs(a_2)
b = abs(b_1) + abs(b_2)

print(longer_line(x, y, a, b))
