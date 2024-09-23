def sum_rec(n: int) -> int:
    if n == 3:
        return n*n*(n*n - 3)
    else:
        return n*n*(n*n - 3) + sum_rec(n-1)
def main():
    numbers = []
    while True:

        m = input()
        if m =="STOP" :

            break
        else:
            m1= int(m)
            numbers.append(sum_rec(m1))
        for i in numbers:
            print(i, end=" ")
if __name__ == '__main__':
    main()
