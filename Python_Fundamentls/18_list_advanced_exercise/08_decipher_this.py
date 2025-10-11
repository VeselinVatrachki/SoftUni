secret_message = input().split()
message = []
numbers = []
words = []
for word in secret_message:
    num = ""
    letters = ""
    for char in word:
        if char.isdigit():
            num += char
        else:
            letters += char
    numbers.append(int(num))
    if len(letters) > 1:
        letters = f"{letters[-1]}{letters[1:-1]}{letters[0]}"
    words.append(letters)

for words, number in zip(words, numbers):
    print(f"{chr(number)}{words}", end=" ")