import sys
def apply_integer_division() -> list:
    li = []
    argc = len(sys.argv)

    if argc < 3:
        print("usage: python script.py <division_factor> <value1> <value2> ...")
        sys.exit(1)

    div = int(sys.argv[1])
    for i in range(2,argc):
        num = float(sys.argv[i])/div
        li.append(num)
    return li
def main():
    lst = apply_integer_division()
    for i in range(len(lst)):
        if i < len(lst)-1:
            print('{0:.3f}'.format(lst[i]),end=', ')
        else:
            print('{0:.3f}'.format(lst[i]))

if __name__ == '__main__':
    main()
