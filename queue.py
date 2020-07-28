from operator import ixor 
n=int(input(""))
l=[0 for i in range(int(n/1.5))]
i=len(n)
for _ in range(n):
    q=[int(x) for x in (input("").split())]
    f=q[0]
    if(f == 2):
        l.append(q[1])
    elif(f==1):
        i-=1
        l[i]=q[1]
        
    else:
        a=q[1]
        b=q[2]
        qq=l[a-1:b]
        res = reduce(ixor, qq) 
    #print(l)
