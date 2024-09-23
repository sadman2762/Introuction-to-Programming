import sys
attractions = {}
for line in sys.stdin:
    data = line.split(":")
    city = data[0]
    attraction = data[1].split(",")
    num_of_attr = len(attraction)
    if city in attractions:
        attractions[city] += num_of_attr
    else:
        attractions[city] = num_of_attr
for key,value in sorted(attractions.items(),key=lambda x:(x[1],x[0])):
    print(f"{key}:{value} attraction(s)")
