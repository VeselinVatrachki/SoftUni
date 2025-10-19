line = input()
number, letters, other = "", "", ""

for char in line:
    if char.isdigit():
        number += char
    elif char.isalpha():
        letters += char
    else:
        other += char

print(number)
print(letters)
print(other)
