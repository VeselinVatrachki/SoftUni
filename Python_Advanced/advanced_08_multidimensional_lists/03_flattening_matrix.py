n = int(input())

matrix = []
flat_result = []
for i in range(n):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)
    flat_result.extend(row_data)
print(flat_result)

# for row in matrix:
#     for el in row:
#         flat_result.append(el)

# print(flat_result)
flat_result = [el for row in matrix for el in row]
print(flat_result)

# read matrix as comprehension

matrix = [[int(el) for el in input().split(", ")] for i in range(n)]