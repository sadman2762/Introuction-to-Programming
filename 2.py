sum = 0

while True:

    n = input()
    if n == "STOP":
        break
    else:
        n1 = n.split()
        for number in n1:
            if int(number) % 7 == 0:
                sum += int(number)

print(sum)



