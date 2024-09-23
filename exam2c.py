import sys
child = {}
for line in sys.stdin:
    data = line.split(':')
    name = data[0]
    fruits = data[1].split(',')
    num_of_fruits = len(fruits)

    if name in child:
        child[name] += num_of_fruits
    else:
        child[name] = num_of_fruits
for key,value in sorted(child.items(),key=lambda x:(x[1],x[0])):
    print(f"{key}:{value} child")
