users_points_dict = {}
courses_dict = {}

while True:
    current_result = input().split("-")

    if len(current_result) == 1:
        break
    elif len(current_result) == 2:
        name = current_result[0]
        del users_points_dict[name]
    else:
        name, course, points = current_result[0], current_result[1], int(current_result[2])
        if name not in users_points_dict.keys():
            users_points_dict[name] = 0
        if users_points_dict[name] < points:
            users_points_dict[name] = points
        if course not in courses_dict.keys():
            courses_dict[course] = 0
        courses_dict[course] += 1

print("Results:")
for name, max_points in users_points_dict.items():
    print(f"{name} | {max_points}")
print("Submissions:")
for course, number_of_students in courses_dict.items():
    print(f"{course} - {number_of_students}")
