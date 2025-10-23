# empty_stack = []
# n = int(input())
#
# for _ in range(n):
#     query = input().split()
#     if query[0] == '1':
#         empty_stack.append(int(query[1]))
#     elif empty_stack:
#         if query[0] == '2':
#             empty_stack.pop()
#         elif query[0] == '3':
#             print(max(empty_stack))
#         elif query[0] == '4':
#             print(min(empty_stack))
#
# #print(', '.join([str(x) for x in reversed(empty_stack)]))
# print(', '.join(map(str, reversed(empty_stack))))


my_stack = []
n = int(input())

function = {
    '1': lambda x: my_stack.append(int(x)),
    '2': lambda: my_stack.pop() if my_stack else None,
    '3': lambda: print(max(my_stack)) if my_stack else None,
    '4': lambda: print(min(my_stack)) if my_stack else None,
}

for i in range(n):
    query = input().split()
    function[query[0]](*query[1:])

print(*reversed(my_stack), sep=', ')