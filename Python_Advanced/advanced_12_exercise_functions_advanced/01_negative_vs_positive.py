def nums_sums(*args):
    negative_sum = sum(n for n in args if n < 0)
    positive_sum = sum(n for n in args if n > 0)

    return negative_sum, positive_sum


nums = map(int, input().split())
negative_numbers, positive_numbers = nums_sums(*nums)

print(negative_numbers)
print(positive_numbers)
if abs(negative_numbers) > abs(positive_numbers):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
    