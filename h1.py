l = []
while True:
    try:
        n = input().split()
        a = int(n[0])
        b = int(n[1])
        c = int(n[2])
        if a**2 + b**2 == c**2:
            l.append("YES")
        else:
            l.append("NO")
    except EOFError:
        break
for r in l:
    print(r)
