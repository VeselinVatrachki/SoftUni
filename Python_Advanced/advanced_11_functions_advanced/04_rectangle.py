# def rectangle(length, width):
#     try:
#         area = length * width
#         perimeter = 2 * (length + width)
#     except:
#         return "Enter valid values!"
#
#     return f"Rectangle area: {area}\nRectangle perimeter: {perimeter}"
#


def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"


    def area():
        return length * width


    def perimeter():
        return 2 * (length + width)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle(2, 10))
print(rectangle('2', 10))