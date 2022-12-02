num = int(input())

students = {}

for i in range(num):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []

    students[student_name].append(grade)

for student in students.keys():
    average_grade = sum(students[student]) / len(students[student])
    if average_grade >= 4.50:
        print(f'{student} -> {average_grade:.2f}')
