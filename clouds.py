n = int(input())

c = list(map(int, input().rstrip().split()))
i=0
co=0
c.append(2)
c.append(2)
while(i<n):
    print(i)
    if(c[i+2]==1):
        i=i+1
        co=co+1

    elif(c[i+1]==1):
        i=i+2
        co=co+1
    elif(c[i+2]==0):
        i=i+2
        co=co+1
    else:
        i=i+1
print(co)

