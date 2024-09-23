import sys
child = {}

for line in sys.stdin:
    data = line.split(":")
    name = data[0];
    project = data[1].split(",")
    num_of_project = len(project)

    if name in child:
        child[name] += num_of_project
    else:
        child[name] = num_of_project
for key,value in sorted(child.items(),key=lambda x:(x[1],x[0])):
    print(f"{key}:{value} project(s)")
