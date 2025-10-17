n = int(input())
students_record = {}

for _ in range(n):
    student = input()
    grade = float(input())

    students_record[student] = students_record.get(student, {})
    students_record[student][grade] = grade #students_record[student].get(grade, 0) + grade

for student in students_record:
    average_grade = sum(students_record[student].values()) / len(students_record[student])
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")