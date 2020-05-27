n,k=[int(x) for x in (input("").split())]
a=[]
f=0
for _ in range(n):
    w=int(input(""))
    if(w>k):
        a.append(w)
        f=1
    else:
        if(f==1):
            a.append(w)
while(1):
    
    if(a[-1]<=k):
        
        a.pop()
    else:
        break

print(len(a))
