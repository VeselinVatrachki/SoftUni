some_string = input()
final_string = ""
last_char = ""
for char in some_string:
    if char != last_char:
        final_string += char
        last_char = char
print(final_string)