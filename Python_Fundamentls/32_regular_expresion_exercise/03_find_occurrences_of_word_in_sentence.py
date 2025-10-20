import re

line = input()
word_for_search = input()
#pattern_name = fr"(?i)\b{word_for_search}\b"
pattern = fr'\b{word_for_search}\b'
matches = re.findall(pattern, line, re.IGNORECASE)
print(len(matches))
