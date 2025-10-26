rows, columns = [int(num) for num in input().split()]

matrix = [[int(num) for num in input().split()] for row in range(rows)]
result = -181
max_column_position = 0
max_row_position = 0
for row in range(rows - 2):
    for col in range(columns - 2):
        sum_numbers = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                sum_numbers += matrix[i][j]
        if sum_numbers > result:
            result = sum_numbers
            max_column_position = col
            max_row_position = row

print(f"Sum = {result}")
for row in range(max_row_position, max_row_position + 3):
    for col in range(max_column_position, max_column_position + 3):
        print(matrix[row][col], end=" ")
    print()
