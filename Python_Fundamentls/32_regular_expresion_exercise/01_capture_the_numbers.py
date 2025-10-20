import re

data = input()
while data:

    pattern = r'\d+'
    matches = re.findall(pattern, data)
    if matches:
        print(" ".join(matches), end=" ")

    data = input()
