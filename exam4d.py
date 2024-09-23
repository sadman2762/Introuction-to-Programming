import sys

def apply_n_root() -> list:
    li = []
    argc = len(sys.argv)
    if argc < 3:
        print("usage python script.py <n_root_factor> <value1> value<2> ...")
        sys.exit(1)
    fac = float(sys.argv[1])
    for i in range(2,argc):
        num = pow(float(sys.argv[i]),1/fac)
        li.append(num)
    return li
def main():
    lst= apply_n_root()
    for i in range(len(lst)):
        if i < len(lst)-1:
            print("{0:.3f}".format(lst[i]),end=' ')
        else:
            print("{0:.3f}".format(lst[i]))
if __name__ == "__main__":
    main()
