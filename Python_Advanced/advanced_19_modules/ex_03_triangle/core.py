def print_upper_part(triangle_size):
    for row in range(1, triangle_size + 1):
        for num in range(1, row + 1):
            print(num, end=' ')
        print()


def print_bottom_part(triangle_size):
    for row in range(1, triangle_size):
        end_num = triangle_size - row
        for num in range(1, end_num + 1):
            print(num, end=' ')
        print()


def print_triangle(triangle_size):

    print_upper_part(triangle_size)
    print_bottom_part(triangle_size)