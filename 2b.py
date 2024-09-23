
l = []

while True:
    s = input()
    if s == "STOP":
        break
    n = s.split()
    counter = 0
    for c in n:
        m = int(c)
        if  m % 10 == 7:
            counter += 1

    l.append(counter)

for r in l:
    print(r)

