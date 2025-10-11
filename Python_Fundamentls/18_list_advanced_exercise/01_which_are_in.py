# def find_substring(substrings_data, string_data):
#     substrings_results = []
#     for current_substring in substrings_data:
#         for current_string in string_data:
#             if current_substring in current_string:
#                 substrings_results.append(current_substring)
#                 break
#
#     return substrings_results
#
# substrings = input().split(", ")
# string = input().split(", ")
# result = find_substring(substrings, string)
# print(result)

def find_substrings(substrings_data, strings_data):
    return [current_substring for current_substring in substrings_data
            if any(current_substring in current_string for current_string in strings_data)]

substrings = input().split(", ")
string = input().split(", ")
result = find_substrings(substrings, string)
print(result)