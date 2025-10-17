# char_list = input().split(", ")
# result = {}
# for i in char_list:
#     key = i
#     if key not in result:
#         result[key] = 0
#
# final_result = {key: ord(key) for key,value in result.materials()}
# print(final_result)
#

char_dict = {char: ord(char) for char in input().split(", ")}
print(char_dict)