number = int(input())
word = input()
strings = []
for _ in range(number):
    lines = input()
    strings.append(lines)
print(strings)
for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)
