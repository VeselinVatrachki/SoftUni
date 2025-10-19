line = input().split()
total_sum = 0

for current_line in line:
    first_letter = current_line[0]
    last_letter = current_line[-1]
    number = int(current_line[1:len(current_line)-1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += number * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position

print(f"{total_sum:.2f}")