def rec_sum(n: int) -> int:
    if n == 2:
        return .5 * (n*n*n - 5*n)
    else:
        return .5 * (n*n*n -5*n) + rec_sum(n-1)
def main():
    numbers = []
    while True:
        m = int(input())
        if m == 0:
            break
        numbers.append(int(rec_sum(m)))
    for i in numbers:
        print(i,end=' ')
if __name__ == '__main__':
    main()
