def is_perfect_number(number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_sum += divisor
    if number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect_number(number))
