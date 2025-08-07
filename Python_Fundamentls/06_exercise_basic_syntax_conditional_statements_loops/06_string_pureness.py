number_of_strings = int(input())

for strings in range(number_of_strings):
    string = input()
    for letter in string:
        if letter == ',' or letter == '.' or letter == '_':
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")

#   Second version!!!
#
# number_of_strings = int(input())
# for strings in range(number_of_strings):
#     string = input()
#     if "," in string or \
#             "." in string or \
#             "_" in string:
#         print(f"{string} is not pure!")
#     else:
#         print(f"{string} is pure.")
