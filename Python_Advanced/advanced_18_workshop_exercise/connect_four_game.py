class InvalidColumnsError(Exception):
    pass

class FullColumnsError(Exception):
    pass

def print_matrix(ma):
    for el in ma:
        print(el)


def validate_column_choice(column_choice, columns):
    if not 0 <= column_choice <= columns:
        raise InvalidColumnsError


def place_player_choice(matrix, column_choice, player_n):
    row_count = len(matrix)
    for row_index in range(row_count -1, -1, -1):
        curr_element = matrix[row_index][column_choice]
        if curr_element == 0:
            matrix[row_index][column_choice] = player_n
            return row_index, column_choice
    raise FullColumnsError


def is_player_num(ma, r, c, player_n):
    if c < 0 or r < 0:
        return False
    try:
        if ma[r][c] == player_n:
            return True
    except IndexError:
        return False
    return False


def is_vertical_win(ma, r, c, player_n, slots):
    return all([is_player_num(ma, r+i, c, player_n) for i in range(slots)])


def is_horizontal_win(ma, r, c, player_n, slots):
    right = []
    for i in range(slots):
        if is_player_num(ma, r, c + i, player_n):
            right.append(True)
        else:
            break

    left = []
    for i in range(slots):
        if is_player_num(ma, r, c - i, player_n):
            left.append(True)
        else:
            break

    return len(left + right) > slots


def is_right_diagonal(ma, r, c, player_n, slots):
    right_up = [is_player_num(ma, r - i, c + i, player_n) for i in range(slots)].count(True)
    left_down = [is_player_num(ma, r + i, c - i, player_n) for i in range(slots)].count(True)
    return (right_up + left_down) > slots


def is_left_diagonal(ma, r, c, player_n, slots):
    right_down = [is_player_num(ma, r + i, c + i, player_n) for i in range(slots)].count(True)
    left_up = [is_player_num(ma, r - i, c - i, player_n) for i in range(slots)].count(True)


def is_winner(ma, r, c, player_n, slots=4):
    if any([
        is_vertical_win(ma, r, c, player_n, slots),
        is_horizontal_win(ma, r, c, player_n, slots),
        is_right_diagonal(ma, r, c, player_n, slots),
        is_left_diagonal(ma, r, c, player_n, slots)
    ]):
        return True
    return False


rows = 6
columns = 7

matrix = [[0 for _ in range(columns)] for i in range(rows)]

print_matrix(matrix)

player_num = 1
count_moves = 0

while True:

    player_num = 2 if player_num % 2 == 0 else 1
    try:
        column_choice = int(input(f'Player {player_num}, Please enter column number from 1 to 7: ')) - 1
        validate_column_choice(column_choice, columns -1)
        row, col = place_player_choice(matrix, column_choice, player_num)
        print_matrix(matrix)

        if is_winner(matrix, row, col, player_num, slots=4):
            print(f'The winner is player {player_num}')
            break

    except InvalidColumnsError:
        print(f"Please enter a valid column number between 1 and {columns}")
        continue
    except FullColumnsError:
        print("Please enter a different column number")
        continue
    except ValueError:
        print("Please enter a valid column number")
        continue

    count_moves += 1
    if rows * columns == count_moves:
        print("The game is draw!")
        break

    player_num += 1

