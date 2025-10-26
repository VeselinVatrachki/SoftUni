rows, columns = [int(num) for num in input().split()]

matrix = [[char for char in input().split()] for row in range(rows)]
result = 0
for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row][col] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            result += 1

print(result)
