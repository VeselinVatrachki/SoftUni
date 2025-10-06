def tribunacci_sequence(n):
    tribunacci = [1, 0, 0]
    for i in range(n):
        num = sum(tribunacci)
        print(num, end=" ")
        tribunacci.append(num)
        tribunacci.pop(0)


number = int(input())
tribunacci_sequence(number)