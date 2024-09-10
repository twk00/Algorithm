n = int(input())
students = {}

for _ in range(n):
    name, korean, english, math = input().split()
    students[name] = (int(korean), int(english), int(math))

sorted_students = sorted(students.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))

for student in sorted_students:
    print(student[0])
