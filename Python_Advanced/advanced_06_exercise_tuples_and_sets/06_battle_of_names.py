the_odd_set = set()
the_even_set = set()

for row in range(1, int(input()) + 1):
    current_sum = sum(ord(ch) for ch in input()) // row
    if current_sum % 2 == 0:
        the_even_set.add(current_sum)
    else:
        the_odd_set.add(current_sum)

if sum(the_odd_set) == sum(the_even_set):
    print(*the_odd_set.union(the_even_set), sep=", ")
elif sum(the_even_set) < sum(the_odd_set):
    print(*the_odd_set.difference(the_even_set), sep=", ")
else:
    print(*the_even_set.symmetric_difference(the_odd_set), sep=", ")
