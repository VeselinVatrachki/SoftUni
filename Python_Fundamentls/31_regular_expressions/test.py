# # # # # coding=utf8
# # # # # the above tag defines encoding for this document and is for Python 2.x compatibility
# # # #
# # # # import re
# # # #
# # # # regex = r"\W+"
# # # #
# # # # test_str = "SoftUni 123 example 1 for test 23 and test 46 !!!"
# # # #
# # # # matches = re.findall(regex, test_str, re.MULTILINE)
# # # #
# # # # print(matches)
# # #
# # # import re
# # #
# # # def test_regex_patterns(regex, string):
# # #     match = re.findall(regex, string)
# # #     if match:
# # #         print('Match found:', match)
# # #     else:
# # #         print('No match found!')
# # #
# # # test_regex_patterns(r'\w+', "SoftUni 123 example 1 for test 23 and test 46 !!!")
# #
# # import re
# #
# #
# # text = 'The ball is red and big'
# # result = re.findall('(red|blue) and (big|small)', text)
# # print(result)
# #
# # import re
# #
# # text = '_ (Underscores) are also word character'
# # result = re.findall('\\w+', text)
# # print(result)
# import re
#
# emails = ['valid123@email.bg', 'invalid*name@emai1.bg', 'example@amazon.co.uk']
#
# pattern_name = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
#
# for email in emails:
#     if re.match(pattern_name, email):
#         print(f"{email} is valid!")
#     else:
#         print(f"{email} is invalid!")



# import re
#
# text = 'The quick brown fox jumps over the lazy dog.'
# result = re.compile(r'fox')
#
# search = result.search(text)
# if search:
#     print('Compiled search found:', search)
# else:
#     print('No search found')
#
import re

text = 'Apple, apple and APPLE are the same fruit.'

pattern = r'apple'
match = re.findall(pattern, text, re.IGNORECASE)

print(match)