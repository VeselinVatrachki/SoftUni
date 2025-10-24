number_of_names = int(input())
names = set()
for _ in range(number_of_names):
    data = input()
    names.add(data)

for name in names:
    print(name)