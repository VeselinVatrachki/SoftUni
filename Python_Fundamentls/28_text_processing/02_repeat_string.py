sequence_of_strings = input().split()
result = [text * len(text) for text in sequence_of_strings]
print(''.join(result))
