dic = {}
with open("clothes.txt") as file:
    for line in file:
        data = line.strip('\n').split(';')
        brand = data[0]
        prices =  int(data[3])
        mul = int(data[2])

        if brand in dic:
            dic[brand] += prices*mul
        else:
            dic[brand] = prices*mul
    for key,value in sorted(dic.items(),key=lambda x:(-x[1],x[0])):
        print(f"{key}:{value} HUF")
