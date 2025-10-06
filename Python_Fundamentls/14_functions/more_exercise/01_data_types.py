def data_types(line):
    if line == "int":
        num = int(second_line)
        return num * 2
    elif line == "real":
        num = float(second_line)
        return f"{(num * 1.5):.2f}"
    elif line == "string":
        line_string = str(second_line)
        return f"${line_string}$"


line = input()
second_line = input()
print(data_types(line))
