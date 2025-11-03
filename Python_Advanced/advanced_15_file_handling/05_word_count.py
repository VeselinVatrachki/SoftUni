import re

with open("words.txt") as file:
    words = file.read().split()

with open("text.txt") as file:
    content = file.read()

occ = {}

for word in words:
    pattern = re.compile(f"\\b{word}\\b", flags=re.IGNORECASE)
    #pattern = rf"\b{word}\b"
    founded = re.findall(pattern, content)
    occ[word] = len(founded)

sorted_occ = sorted(occ.items(), key=lambda x: x[1], reverse=True)
with open("output.txt", "w") as file:
    for key, value in sorted_occ:
        file.write(f"{key} - {value}\n")