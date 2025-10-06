def absolute_values():
    list_sequence_of_numbers = input().split()
    numbers = []
    for num in list_sequence_of_numbers:
        numbers.append(abs(float(num)))
    print(numbers)

absolute_values()
