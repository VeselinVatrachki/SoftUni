def create_sequence(n):
    first_number = 0
    second_number = 1

    seq = [first_number, second_number]

    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq


def locate_index_of_number(seq, number):
        return seq.index(number)
