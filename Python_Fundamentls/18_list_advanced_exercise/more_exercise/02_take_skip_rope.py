string_input = input()

numbers = []
letter = ""
take_list = []
skip_list = []

final_result = ""

for char in string_input:
    if char.isdigit():
        numbers.append(int(char))
    else:
        letter += char

for index, number in enumerate(numbers):
    if index % 2 == 0:
        take_list.append(number)
    else:
        skip_list.append(number)

for i, n in zip(take_list, skip_list):
    if i == 0:
        letter = letter[n:]
    elif i != 0:
        final_result += letter[:i]
        letter = letter[n + i:]

print(final_result)
