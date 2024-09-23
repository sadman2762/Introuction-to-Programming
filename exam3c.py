def rec_sum(n: int) -> int:
    if n == 3:
        return 45
    else:
        return n*n*(n*n-4) + rec_sum(n-1)
def main():
    numbers=[]
    while True:
        m = int(input())
        if m == 0:
            break
        numbers.append(rec_sum(m))
    for i in numbers:
        print(i,end=' ')
if __name__ =='__main__':
    main()
