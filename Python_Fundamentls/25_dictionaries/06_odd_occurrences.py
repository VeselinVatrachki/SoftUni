line = input().split()
result = {}
for word in line:
    word_lower = word.lower()
    if word_lower not in result:
        result[word_lower] = 0
    result[word_lower] += 1

for k, v in result.items():
    if v % 2 != 0:
        print(k, end=" ")
