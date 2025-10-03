numbers = input().split()
num_to_remove = int(input())
lst_integer = []
for num in numbers:
    lst_integer.append(int(num))
for _ in range(num_to_remove):
    m = min(lst_integer)
    lst_integer.remove(m)
final_numbers = ", ".join(map(str, lst_integer))
print(final_numbers)
