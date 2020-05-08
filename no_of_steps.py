n=int(input(""))

a=[int(x) for x in(input("").split())]
b=[int(x) for x in(input("").split())]
mi=min(a)
c=0
for i in range(n):
    while(a[i]>mi):
        a[i]-=b[i]
        c+=1
        
        if(a[i]<mi):
            print(-1)
    
            exit(0)
    
print(c)