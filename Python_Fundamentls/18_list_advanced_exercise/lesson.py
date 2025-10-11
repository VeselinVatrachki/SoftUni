# # # # even_numbers = (x for x in range(1, 10) if x % 2 == 0)
# # # # print(even_numbers)
# # #
# # #
# # # multiplication_table = [[x * y for x in range(1, 6)] for y in range(1, 6)]
# # # print(multiplication_table)
# #
# #
# # matrix = [[j for j in range(5)] for i in range(5)]
# # print(matrix)
#
# # unique_chars = {char for char in "Hello World"}
# # print(unique_chars)
#
# # print(set(list([0,1,1,1,2,2,2,3,3,3,4,4,4])))
#
#
# #      numbers = list(map(int, input().split(", ")))
# #      print(numbers)
#
# numbers = [1, 2, 3, 4, 5]
# even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))
# even_numbers_map = list(map(lambda num: num % 2 == 0, numbers))
# print("filter ->", even_numbers_filter)
# print("map ->", even_numbers_map)

# numbers = [1, 2, 3, 4, 5]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# sorted_numbers.reverse()
# print(sorted_numbers)

# fruits = ["apple", "banana", "cherry", "strawberry"]
# print(sorted(fruits, key=len))
# print(sorted(fruits, reverse=True))
# print(sorted(fruits))