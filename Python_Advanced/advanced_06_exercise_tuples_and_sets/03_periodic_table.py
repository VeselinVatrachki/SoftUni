# # n = int(input())
# #
# # element = set()
# # for _ in range(n):
# #     chemical_compounds = input().split()
# #     for element in chemical_compounds:
# #         element.add(element)
# #
# # print(*element, sep='\n')
#
#
#                  ####################################
#
# element = set()
#
# for _ in range(int(input())):
#     for el in input().split():
#         element.add(el)
#
# print(*element, sep='\n')


                     ######################################

print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")
