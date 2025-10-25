row, column = [int(x) for x in input().split(", ")]

matrix = []
matrix_sum = 0

for row in range(row):
    data = [int(el) for el in input().split(", ")]
    matrix_sum += sum(data)
    matrix.append(data)

print(matrix_sum)
print(matrix)
