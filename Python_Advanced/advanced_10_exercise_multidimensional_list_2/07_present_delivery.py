presents = int(input())
n = int(input())

matrix = []
santa = []
good_kids = 0
good_kids_gifted = 0
directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for r in range(n):
    matrix.append(input().split())
    for c in range(n):
        if matrix[r][c] == "S":
            santa = [r, c]
        elif matrix[r][c] == "V":
            good_kids += 1

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    r, c = santa[0] + directions[command][0], santa[1] + directions[command][1]
    if 0 <= r < n and 0 <= c < n:
        if matrix[r][c] == "V":
            presents -= 1
            good_kids_gifted += 1
            matrix[r][c] = "-"
        elif matrix[r][c] == "C":
            for direction in directions.values():
                next_r, next_c = r + direction[0], c + direction[1]
                if matrix[next_r][next_c] in "VX" and presents > 0:
                    presents -= 1
                    if matrix[next_r][next_c] == "V":
                        good_kids_gifted += 1
                    matrix[next_r][next_c] = "-"
        matrix[santa[0]][santa[1]] = "-"
        santa = [r, c]
        matrix[r][c] = "S"

gifts = good_kids - good_kids_gifted

if presents < 1 and gifts > 0:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row)
if gifts > 0:
    print(f"No presents for {gifts} nice kid/s.")
else:
    print(f"Good job, Santa! {good_kids_gifted} happy nice kid/s.")
