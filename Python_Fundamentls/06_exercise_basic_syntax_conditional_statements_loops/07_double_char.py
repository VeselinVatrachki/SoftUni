# current_string = input()
# while current_string != "End":
#     if current_string != 'SoftUni':
#         for char in current_string:
#             print(char * 2, end="")
#         print()
#     current_string = input()


current_string = input()
while current_string != "End":
    if current_string != "SoftUni":
        new_string = ""
        for char in current_string:
            new_string += char * 2
        print(new_string)
    current_string = input()
