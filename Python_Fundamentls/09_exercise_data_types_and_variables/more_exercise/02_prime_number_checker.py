number = int(input())
not_prime = False
if number == 1:
    print("False")
else:
    for num in range(2, number):
        if number % num == 0:
            not_prime = True
            break
    if not_prime:
        print("False")
    else:
        print("True")
