n=int(input(""))
a=[int(x) for x in (input("").split())]
x=[0]
def ab(k,l):
    e=abs(sum(k)-sum(l))
   
    x.append(e)
    
i=-1
j=-1
while(i+2<n):
    i+=1
    j=i+1
    
    while(j<n-1):
        j=j+1
        k=j+1
        while(k-1<n):
            ab(a[i:j],a[j:k])
            
            k+=1

print(max(x))