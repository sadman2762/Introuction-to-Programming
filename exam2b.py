import sys
man = {}
for line in sys.stdin:
    data = line.split(":")
    name = data[0]
    device = data[1].split(",")
    num_of_devices = len(device)

    if name in man:
        man[name] += num_of_devices
    else:
        man[name] = num_of_devices
for key,value in sorted(man.items(),key=lambda x:(x[1],x[0])):
    print(f"{key}:{value}toys ")
