n=int(input(""))
l=[]
m=[]
for _ in range(n):
    
    x=[int(x) for x in (input("").split())]
    c=x[0]
    if(c==1):
        l.append(x[1])
        if len(m)==0 or m[-1]<x[1]: m.append(x[1])

    elif(c==2):
        c=l.pop()
        if c==m[-1]: m.pop()
    else:
        print(m[-1])

f=NULL

