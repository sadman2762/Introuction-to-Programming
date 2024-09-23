sum = 1
while True:
    n = input()
    if n == "0":
        break
    for digit in n:
        if int(digit) % 2 == 0:
            sum *= int(digit)
print(sum)
