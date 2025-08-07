string_word = input().lower()
lst = ["sand", "water", "fish", "sun"]
count = 0

for word in lst:
    if word in string_word:
        words = string_word.count(word)
        count += words
print(count)
