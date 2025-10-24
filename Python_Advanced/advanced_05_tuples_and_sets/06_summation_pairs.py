# numbers = list(map(int, input().split()))
# target_number = int(input())
#
# for first_number in range(len(numbers)):
#     for second_number in range(first_number + 1, len(numbers)):
#         if numbers[first_number] + numbers[second_number] == target_number:
#             print(f"{numbers[first_number]} + {numbers[second_number]} = {target_number}")



            ########################################


numbers = list(map(int, input().split()))
target = int(input())

targets = set()
values = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values[value]
        del values[value]
        print(f"{pair} + {value} = {target}")
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values[resulting_number] = value
