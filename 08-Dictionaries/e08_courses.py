courses = {}

while True:
    user_input = input()

    if user_input == 'end':
        break

    current_entry = user_input.split(' : ')

    course_name = current_entry[0]
    student_name = current_entry[1]

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

for course in courses.keys():
    number_of_students = len(courses[course])
    print(f'{course}: {number_of_students}')
    [print(f'-- {student}') for (student) in courses[course]]
    