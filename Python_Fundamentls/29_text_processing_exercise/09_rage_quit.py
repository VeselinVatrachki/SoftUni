text = input()
final_msg = ""
sub_string = ""
repetitions = ""

for index in range(len(text)):

    if not text[index].isdigit():
        sub_string += text[index].upper()
    else:
        for next_char in range(index, len(text)):
            if not text[next_char].isdigit():
                break
            repetitions += text[next_char]
        final_msg += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(final_msg))}")
print(final_msg)
