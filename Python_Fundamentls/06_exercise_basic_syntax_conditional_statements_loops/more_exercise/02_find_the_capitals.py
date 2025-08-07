# # single_string = input()
# # new_string = single_string.strip()
# # for char in new_string:
# #     if char.isupper():
# #
#


# input_string = input("Enter any string: ")
# indices = [i for i, char in enumerate(input_string) if char.isupper()]
# print(indices)

input_string = input()
list_capital = []
for value, char in enumerate(input_string):
    if char.isupper():
        list_capital.append(value)
print(list_capital)
