sequence_of_numbers = input().split()
middle = len(sequence_of_numbers) // 2
left_side = 0
right_side = 0
for number in sequence_of_numbers[:middle]:
    left_side += int(number)
    if number == "0":
        left_side -= (left_side * 0.2)
for number in sequence_of_numbers[middle + 1:][::-1]:
    right_side += int(number)
    if number == "0":
        right_side -= (right_side * 0.2)
if left_side < right_side:
    print(f"The winner is left with total time: {left_side:.1f}")
elif left_side > right_side:
    print(f"The winner is right with total time: {right_side:.1f}")
