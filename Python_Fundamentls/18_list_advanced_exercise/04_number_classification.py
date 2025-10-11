nums = list(map(int, input().split(", ")))

POSITIVE = [str(num) for num in nums if num >= 0]
NEGATIVE = [str(num) for num in nums if num < 0]
EVEN = [str(num) for num in nums if num % 2 == 0]
ODD = [str(num) for num in nums if num % 2 != 0]

print(f'Positive: {", ".join(POSITIVE)}')
print(f'Negative: {", ".join(NEGATIVE)}')
print(f'Even: {", ".join(EVEN)}')
print(f'Odd: {", ".join(ODD)}')
