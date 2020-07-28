n= int(input(""))
di=[]
l=[]
for _ in range(n):
    
    di.append(input(""))
    l.append(float(input("")))
x=l.index(min(l))
l[x]=999999     
di[x]='zzzzzzzz'
v=min(l)
mini="zzzzzzz"
x=[]
for i in range(n):
    if(l[i]==v):
        x.append(di[i])
x.sort()
print(x)



