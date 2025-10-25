n = int(input())

matrix = [[int(el) for el in input().split()] for j in range(n)]
diagonal_sum = 0

#matrix = matrix[::-1]      for opposite diagonals ( from index 0:2, 1:1, 2:0 )

# for row_index in range(n):
#     for col_index in range(n):
#         if row_index == col_index:
#             diagonal_sum += matrix[row_index][col_index]

for index in range(n):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)

