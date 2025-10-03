string = input().split(", ")
back_index = 0

for i in string:
    if i == "0":
        back_index -= 1
        string.remove(i)
        string.append("0")

result = [int(num) for num in string]
print(result)
