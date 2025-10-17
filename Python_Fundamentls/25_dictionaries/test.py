# # keys = ["name", "age", "major"]
# # values = ["Ivan", "23", "Developer"]
# #
# # student = dict(zip(keys, values))
# # print(student)
# #
# # my_dict = {
# #     "fruit": "apple",
# #     "vegetable": "carrot",
# #     "diary": "milk",
# # }
# #
# # print(my_dict)
# #
#
# my_dict = {'name': 'Ivan', 'age': '23', 'major': 'Developer'}
#
# for key, value in my_dict.materials():
#     print(f'{key}: {value}')
#
# student_grades = {
#     'Ivan': 6,
#     'Pesho': 5,
#     'Gosho': 4,
#     'Maria': 3,
#     'Ana': 2,
# }
# for name, grade in student_grades.materials():
#     print(f'Student {name}: Grade {grade}')

### DICTIONARY COMPREHENSION ###

fruits = ["apple", "banana", "cherry", "strawberry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)

### DICTIONARY COMPREHENSION ###

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = {num: num ** 2 for num in numbers if num % 2 == 0}
print(squares)