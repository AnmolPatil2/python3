t=int(input(""))
for _ in range(t):
    sum1=0
    a,b=[int(x) for x in (input("").split())]
    if(a>1000000000):
        for x in range(a,b+1):
            sum1+=x
        dif=b-a+1
        int(sum1/dif)
    else:
        print(int((a+b)/2))
