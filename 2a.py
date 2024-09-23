def sum5(n: int) -> int:
    if n == 2:
        return -22
    else:
        return -n * (n + 9) + sum5(n - 1)
def main():
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            return sum5(n)
        print(sum5(n))
main()
