def sorted_numbers(numbers: int):
    return sorted(numbers)


numbers_as_digit = input().split()
list_numbers = []
for number in numbers_as_digit:
    list_numbers.append(int(number))
print(sorted_numbers(list_numbers))
