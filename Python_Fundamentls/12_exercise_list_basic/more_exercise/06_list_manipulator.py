numbers = [int(num) for num in input().split()]
command = input().split()

while command[0] != "end":

    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]

    if command[0] == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers):
            numbers = numbers[:index +1] + numbers[index + 1:]
        else:
            print("Invalid index")

    

    command = input().split()