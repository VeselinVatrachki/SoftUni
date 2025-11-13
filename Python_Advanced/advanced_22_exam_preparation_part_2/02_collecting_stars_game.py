n = int(input())

matrix = []
player_position = []
stars = 2

for row in range(n):
    data = input().split()
    if "P" in data:
        player_position = [row, data.index("P")]
        matrix[row][data.index("P")] = "."
    matrix.append(data)

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while 0 < stars < 10:
    command = input()
    next_row = player_position[0] + moves[command][0]
    next_col = player_position[1] + moves[command][1]

    if not(0 <= next_row < n and 0 <= next_col < n):
        next_row, next_col = 0, 0

    if matrix[next_row][next_col] == "*":
        stars += 1
        matrix[next_row][next_col] = "."
    elif matrix[next_row][next_col] == "#":
        stars -= 1
        continue

    player_position = [next_row, next_col]

if stars:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")
print(f"Your final position is [{player_position[0]}, {player_position[1]}]")

matrix[player_position[0]][player_position[1]] = "P"
for row in matrix:
    print(" ".join(row))