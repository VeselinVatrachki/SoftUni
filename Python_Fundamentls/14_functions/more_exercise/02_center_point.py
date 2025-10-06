from math import floor
def closest_to_center(x_1, y_1, x_2, y_2):
    dist1 = x_1 ** 2 + y_1 ** 2
    dist2 = x_2 ** 2 + y_2 ** 2
    if dist1 <= dist2:
        return f"({floor(x_1)}, {floor(y_1)})"
    elif dist1 == dist2:
        return f"({floor(x_1)})"
    else:
        return f"({floor(x_2)}, {floor(y_2)})"


x_1, y_1 = float(input()), float(input())
x_2, y_2 = float(input()), float(input())
print(closest_to_center(x_1, y_1, x_2, y_2))
