l = []
while True:
    n = input()
    r = ""
    if n == "END":
        break
    s = n
    for c in s:
        if c.isupper():
            r += c * 2
        else:
            r += c
    l.append(r)
for r in l:
    print(r)
