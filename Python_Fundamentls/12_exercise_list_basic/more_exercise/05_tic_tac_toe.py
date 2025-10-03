first_row = input().split()
second_row = input().split()
third_row = input().split()
game_won = "First"
win = False

for player in range(1, 3):
    player = str(player)
    winning_row = [player] * 3
    if any([winning_row == first_row,
            winning_row == second_row,
            winning_row == third_row]):
        win = True
    for index in range(0, 3):
        if all([first_row[index] == player,
               second_row[index] == player,
               third_row[index] == player]):
            win = True
    if all([first_row[0] == player,
            second_row[1] == player,
            third_row[2] == player]):
        win = True
    elif all([first_row[2] == player,
              second_row[1] == player,
              third_row[0] == player]):
        win = True
    if win:
        print(f"{game_won} player won")
        break
    game_won = "Second"
else:
    print("Draw!")
