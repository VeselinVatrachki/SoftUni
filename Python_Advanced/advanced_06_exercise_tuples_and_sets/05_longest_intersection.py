# longest_intersection = set()
#
# for _ in range(int(input())):
#     nums_in_range = input().split("-")
#     first_start, first_end = [int(x) for x in nums_in_range[0].split(",")]
#     second_start, second_end = [int(x) for x in nums_in_range[1].split(",")]
#
#     first_set = set(range(first_start, first_end + 1))
#     second_set = set(range(second_start, second_end + 1))
#
#     intersection = first_set & second_set
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")


               ##############################################
def create_set_from_range(range_str):
    start, end = range_str.split(',')
    return set(range(int(start), int(end) + 1))


longest_intersection = set()

for _ in range(int(input())):
    nums_in_range = input().split("-")

    first_set = create_set_from_range(nums_in_range[0])
    second_set = create_set_from_range(nums_in_range[1])

    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
