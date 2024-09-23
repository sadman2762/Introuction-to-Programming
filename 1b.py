
l = []
while True:
    try:
        n = input()
        product = 1

        for c in n:

            product *= int(c)
        l.append(product)
    except EOFError:
        break


print(max(l))
