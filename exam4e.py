import sys
def apply_exponent() -> list:
    li = []
    argc = len(sys.argv)

    if argc < 3:
        print("usage python script.py <exponent_factor> <value1> <value2> ..")
        sys.exit(1)

    fac = float(sys.argv[1])
    for i in range(2,argc):
        num = pow(fac,float(sys.argv[i]))
        li.append(num)
    return li
def main():
    lst = apply_exponent()
    for i in range(len(lst)):
        if i < len(lst) - 1:
            print("{0:.3f}".format(lst[i]),end=', ')
        else:
            print("{0:.3f}".format(lst[i]))
if __name__ == "__main__":
    main()

