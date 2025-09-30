key = int(input())
number_of_letters = int(input())
message = ""
for _ in range(number_of_letters):
    letter = input()
    code = ord(letter) + key
    message += chr(code)
print(message)
