def odd_and_even_sum(some_number: str):
    sum_of_odd = 0
    sum_of_even = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"


number = input()
print(odd_and_even_sum(number))
