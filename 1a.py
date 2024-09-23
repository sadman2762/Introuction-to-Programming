l = []
k = []
while True:
    sum = 0
    counter = 0
    n = input()
    if n == "0" :
        break
    for c in n :
        sum += int(c)
        counter += 1
    l.append(sum)
    k.append(counter)
print(l[k.index(min(k))])
