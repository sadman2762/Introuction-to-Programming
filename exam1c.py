dic = {}
with open("bicycles.txt") as file:
    for line in file:
        data = line.strip("\n").split(":")
        band = data[1]
        prices = int(data[3])

        if band in dic:
            dic[band] += prices
        else:
            dic[band] = prices
    for key,value in sorted(dic.items(),key=lambda x:(-x[1],x[0])):
        print(f"{key}({value}HUF)")
