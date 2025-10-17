# text = input()
# count_dict = {}
# for char in text:
#     if char == " ":
#         continue
#     else:
#         count_dict[char] = count_dict.get(char, 0) + 1
# for char, count in count_dict.materials():
#     print(f"{char} -> {count}")

line = [character for character in input() if character != " "]
letters = {}
for character in line:
    if character not in letters.keys():
        letters[character] = 0
    letters[character] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")
