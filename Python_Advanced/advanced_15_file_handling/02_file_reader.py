try:
    file = open("numbers.txt")
    total_sum = 0
    for element in file:
        total_sum += int(element)
    print(total_sum)
    file.close()

except FileNotFoundError:
    print("File not found")


###########################################

file = open("numbers.txt")
content = file.read().split()

total_sum = 0
for element in content:
    try:
        total_sum += int(element)
    except ValueError:
        continue

print(total_sum)


##########################################


file = open("numbers.txt")
content = file.readlines()

total_sum = 0

for element in content:
    total_sum += int(element[:-1])

print(total_sum)