num_of_int = int(input())
pos_num = []
neg_num = []
for _ in range(num_of_int):
    number = int(input())
    if number >= 0:
        pos_num.append(number)
    else:
        neg_num.append(number)
print(pos_num)
print(neg_num)
print(f"Count of positives: {len(pos_num)}")
print(f"Sum of negatives: {sum(neg_num)}")
