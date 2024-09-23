dic = {}

with open("books.txt") as file:
    for line in file:
        data = line.strip("\n").split(";")
        writer = data[1]
        if writer in dic:
            dic[writer] += 1
        else:
            dic[writer] = 1
    for key,value in sorted(dic.items(),key=lambda x:(-x[1],x[0])):
        print(f"{key}:{value} book(s) available")
