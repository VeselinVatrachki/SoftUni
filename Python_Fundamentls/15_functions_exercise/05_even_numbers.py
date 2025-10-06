def is_even(n):
    return n % 2 == 0


numbers_as_string = input().split()
list_numbers = []
for number in numbers_as_string:
    list_numbers.append(int(number))
final_list = list(filter(is_even, list_numbers))
print(final_list)
