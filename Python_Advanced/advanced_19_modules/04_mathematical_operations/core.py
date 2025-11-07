from errors import UnknownSignError


def sum_nums(num1, num2):
    return num1 + num2


def subtract(num1, num2):
        return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1 ** num2

mapper = {
    "+": sum_nums,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power
}
def execute(num1, sign, num2):
    if sign in mapper:
        respective_func = mapper[sign]
        return respective_func(num1, num2)
    raise UnknownSignError("Please provide a valid sign")