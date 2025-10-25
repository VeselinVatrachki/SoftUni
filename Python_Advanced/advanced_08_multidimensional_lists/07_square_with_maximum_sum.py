row, column = [int(el) for el in input().split(", ")]

matrix = [[int(el ) for el in input().split(", ")] for _ in range(row)]
max_sum = float("-inf")
sub_matrix = None

for row_index in range(row - 1):
    for col_index in range(column - 1):
        element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        sum_element = element + next_element + element_below + element_diagonal
        if sum_element > max_sum:
            max_sum = sum_element
            sub_matrix = [[element,next_element], [element_below,element_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
