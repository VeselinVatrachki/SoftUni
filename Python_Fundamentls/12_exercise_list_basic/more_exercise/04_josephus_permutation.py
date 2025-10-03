numbers_as_string = input().split()
n_to_get = int(input())
result = []
start_index = n_to_get - 1
index = 0

while numbers_as_string:
    index = (start_index + index) % len(numbers_as_string)
    result.append(numbers_as_string.pop(index))

print(f"[{','.join(result)}]")
