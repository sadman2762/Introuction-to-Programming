import random
n = int(input("n = "))
sum = 0
counter = 0
for i in range(n):
    number = random.randint(25,85)
    print(number,end=" ")
    if number % 2 != 0:
        sum += number
        counter += 1
print("\n{}".format(sum/counter))
