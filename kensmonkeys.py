def check(t):
    print(t)
    for i in range(n):
        if(t[i]!=og[i]):
            return 0
    return 1
t=int(input(""))
for _ in range(t):
    n= int(input(""))
    l=[int(x)-1 for x in (input("").split())]
    og=[i for i in range(n)]

    t1=og.copy()
    t2=[0 for i in range(n)]
    j=0
    while(j<10):
        if(j%2==0):
            for i in range(n):
                
                t2[l[i]]=t1[i]
            
            if(check(t2)):
                print(i)
                i+=1
                exit(0)
        else:
            for i in range(n):
                t1[l[i]]=t2[i]
            if(check(t1)):
                print(i)
                i+=1
                exit(0)
        j+=1
        print(j)
