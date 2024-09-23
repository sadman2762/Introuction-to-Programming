l = []
while True:
    n = input()
    r = ""
    if n == "END":
        break
    for c in n:
        if not c.isnumeric():
            r += c


    l.append(r)

for r in l:
    print(r)

