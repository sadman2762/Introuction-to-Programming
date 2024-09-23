import random
counter = 0
prod = 1
n = int(input("n = "))
for i in range(n):
    number = random.randint(20,70)
    print(number,end=" ")
    if number % 2 ==1:
        prod *= number
        counter += 1
print("\n{0:.2f}".format(pow(prod,(1/counter))))
