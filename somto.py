import sys

children = {}

for line in sys.stdin:
    data = line.strip().split(";")
    names = data[1].split(",")

    for name in names:
        name = name.strip()
        if name in children:
            children[name] += 1
        else:
            children[name] = 1

for key, value in sorted(children.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value} product{'s' if value > 1 else ''}")
