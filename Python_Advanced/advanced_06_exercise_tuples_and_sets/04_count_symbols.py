# # text = input()
# #
# # result = {ch for ch in text}
# #
# # for char in sorted(result):
# #     print(f"{char}: {text.count(char)} time/s")
#
#
# txt = input()
#
# uniq_symbol = sorted(set(txt))
# for ch in uniq_symbol:
#     print(f"{ch}: {txt.count(ch)} time/s")
#

txt = input()
[print(f"{ch}: {txt.count(ch)} time/s") for ch in sorted(set(txt))]
