students = [i for i in range(1, 31)]

for s_students in range(28):
    s_students_num = int(input())
    students.remove(s_students_num)
print(min(students))
print(max(students))