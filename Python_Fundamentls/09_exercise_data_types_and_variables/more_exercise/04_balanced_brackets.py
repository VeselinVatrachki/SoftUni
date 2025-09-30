# number_of_lines = int(input())
# line_string = ""
# for _ in range(number_of_lines):
#     command = input()
#     if command.count('(') != command.count(')'):
#         line_string = "UNBALANCED"
#     elif command.count('(') != command.count(')') and command.count('(') > command.count(')'):
#         line_string = "UNBALANCED"
#     else:
#         line_string = "BALANCED"
# print(line_string)

number_of_lines = int(input())
count = 0
for _ in range(number_of_lines):
    line = input()
    if line == "(":
        count += 1
    elif line == ")":
        count -= 1
    if count > 1 or count < 0:
        break
if count == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
