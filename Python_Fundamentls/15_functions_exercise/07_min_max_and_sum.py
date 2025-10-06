def min_max_and_sum(num):
    return f"The minimum number is {min(num)}\nThe maximum number is {max(num)}\nThe sum number is: {sum(num)}"


numbers_as_string = input().split()
numbers = []
for number in numbers_as_string:
    numbers.append(int(number))
print(min_max_and_sum(numbers))
