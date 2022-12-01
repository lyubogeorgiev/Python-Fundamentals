userInput = input().split(':')
courses = {}

while len(userInput) > 1:
    studentName = userInput[0]
    studentId = userInput[1]
    courseName = userInput[2]

    if courseName not in courses.keys():
        courses[courseName] = {}

    courses[courseName][studentId] = studentName
    userInput = input().split(':')

selectedCourseName = userInput[0].replace('_', ' ')

[print(f'{value} - {key}') for (key, value) in courses[selectedCourseName].items()]
# for (key, value) in courses[selectedCourseName].items():
#     print(f'{value} - {key}')
