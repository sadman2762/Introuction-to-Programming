import sys
students = {}
for line in sys.stdin:
    data = line.strip().split(':')
    student = data[0]
    subjects = data[1].split(',')
    for i in subjects:
        if i in students:
            students[i] += 1
        else:
            students[i] = 1

for key,value in sorted(students.items(),key=lambda x:(-x[1],x[0])):
    print(f"{key}:{value} student(s)")
