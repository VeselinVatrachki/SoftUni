from math import log


num = int(input())

try:
    logarithm_base = int(input())
    print(f"{log(num, logarithm_base):.2f}")
except ValueError:
    print(f"{log(num):.2f}")
