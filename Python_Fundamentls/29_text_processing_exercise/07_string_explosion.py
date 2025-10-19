line = input()
final_string = ""
strength = 0

for index in range(len(line)):
    if strength > 0 and line[index] != '>':
        strength -= 1
    elif line[index] == '>':
        final_string += ">"
        strength += int(line[index+1])
    else:
        final_string += line[index]

print(final_string)
