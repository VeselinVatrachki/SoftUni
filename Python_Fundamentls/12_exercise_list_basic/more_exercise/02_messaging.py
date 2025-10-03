sequence_of_numbers = input().split()
some_string = input()
char = 0
message = ""
for number in sequence_of_numbers:
    index = sum([int(num) for num in number])
    if index >= len(some_string):
        index = index - len(some_string)
    message += some_string[index + char]
    char += 1

print(message)
