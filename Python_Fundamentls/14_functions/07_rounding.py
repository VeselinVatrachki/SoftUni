def rounding_number(numbers):
    number = []
    for nums in numbers:
        num = float(nums)
        number.append(round(num))
    return number


numbers = input().split()
print(rounding_number(numbers))
