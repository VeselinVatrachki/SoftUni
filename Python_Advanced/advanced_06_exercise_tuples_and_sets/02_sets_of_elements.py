numbers = input().split()

first_number = {input() for _ in range(int(numbers[0]))}
second_number ={input() for _ in range(int(numbers[1]))}

uniq_nums = first_number.intersection(second_number)
print(*uniq_nums, sep='\n')
