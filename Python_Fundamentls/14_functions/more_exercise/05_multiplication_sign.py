a = int(input())
b = int(input())
c = int(input())

def multiplication_sign(a, b, c):

    if ( c > 0 and b < 0 and a < 0 or
        b > 0 and a < 0 and c < 0 or
        a > 0 and c < 0 and b < 0 or
        a > 0 and b > 0 and c > 0):
        return "positive"

    elif a == 0 or b == 0 or c == 0:
        return "zero"

    elif a < 0 or b < 0 or c < 0:
        return "negative"


print(multiplication_sign(a, b, c))
