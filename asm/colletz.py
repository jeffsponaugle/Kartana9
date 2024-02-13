def getclen(num):
    if (num==0):
        return 1
    length = 0
    max=0
    current=num
    while (current != 1):
        if current > max: max = current
        length = length + 1
        if ((current&1)==1):
            current = (current * 3) + 1
        else:
            current = (current>>1)
     
    return length,max
total=0
bigmax=0

for i in range(1,256):
    (l,m) = getclen(i)
    print(i,"Steps:",l,"Max:",m)
    total=total+l
    if (m>bigmax): bigmax=m
    if (m>(65536*65535)):
        print("OVERFLOW")
        exit()

print("sum:",total,"max:",bigmax)  
