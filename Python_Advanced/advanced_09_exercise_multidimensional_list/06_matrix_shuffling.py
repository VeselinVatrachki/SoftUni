rows, cols = [int(num) for num in input().split()]

matrix = [[num for num in input().split()] for row in range(rows)]

while True:
    command = input().split()
    cmd = command[0]
    if cmd == 'END':
        break
    elif len(command) != 5 or cmd != 'swap':
        print('Invalid input!')
        continue
    elif cmd == 'swap':
        row_1 = int(command[1])
        col_1 = int(command[2])
        row_2 = int(command[3])
        col_2 = int(command[4])
        if 0 <= row_1 < rows and 0 <= row_2 < rows and 0 <= col_1 < cols and 0 <= col_2 < cols:
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for row in matrix:
                print(' '.join(row))
        else:
            print('Invalid input!')
