dic = {}

with open("album.txt") as file:
    for line in file:
        data = line.strip('\n').split(";")
        band = data[1]
        if band in dic:
            dic[band] += 1
        else:
            dic[band] = 1
    for key,value in sorted(dic.items(),key=lambda x:(-x[1],x[0])):
        print(f"{key}:{dic[key]} album(s) available")
