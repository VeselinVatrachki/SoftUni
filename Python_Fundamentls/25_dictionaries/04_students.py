course_to_search = ""
students = []

while True:
    student_info = input()

    if ":" not in student_info:
        course_to_search = student_info
        break

    name, id_, course = student_info.split(":")
    students.append({'name': name, 'ID': id_, 'course': course})

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")
