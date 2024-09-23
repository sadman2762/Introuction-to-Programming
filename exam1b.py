dic = {}

with open("car.txt") as file:
    for line in file:
        data = line.strip("\n").split(";")
        band = data[1]
        price = int(data[3])

        if band in dic:
            dic[band] += price
        else:
            dic[band] = price
    for key,value in sorted(dic.items(),key=lambda x:(-x[1],x[0])):
        print(f"{key} ({value}EUF)")
