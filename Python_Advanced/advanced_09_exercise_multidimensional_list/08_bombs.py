n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
bombs = input().split()


def bombed_cells(x, y, size):
    cells = []
    '''
    123
    4x5
    678
    '''
    if x - 1 in range(size) and y - 1 in range(size):
        cells.append((x - 1, y - 1))
    if x in range(size) and y - 1 in range(size):
        cells.append((x, y - 1))
    if x + 1 in range(size) and y - 1 in range(size):
        cells.append((x + 1, y - 1))
    if x - 1 in range(size) and y in range(size):
        cells.append((x - 1, y))
    if x + 1 in range(size) and y in range(size):
        cells.append((x + 1, y))
    if x - 1 in range(size) and y + 1 in range(size):
        cells.append((x - 1, y + 1))
    if x in range(size) and y + 1 in range(size):
        cells.append((x, y + 1))
    if x + 1 in range(size) and y + 1 in range(size):
        cells.append((x + 1, y + 1))
    return cells


for bomb in bombs:
    row, col = [int(num) for num in bomb.split(',')]
    curr_bomb = matrix[row][col]
    if curr_bomb > 0:
        neighbour_cells = bombed_cells(row, col, n)
        for r, c in neighbour_cells:
            if matrix[r][c] > 0:
                matrix[r][c] -= curr_bomb
        matrix[row][col] = 0

result_count = 0
result_sum = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            result_count += 1
            result_sum += matrix[row][col]

print(f"Alive cells: {result_count}")
print(f"Sum: {result_sum}")
for row in range(n):
    print(*matrix[row])
