n=int(input(""))
t=[]
for i in range(n):
    l=[int(x) for x in (input("").split())]
    t.append(l)
l=t
j=0
i=0
s=l[0][0]

while(i<n-1 and j<n-1):
    if(l[i+1][j]>=l[i][j+1]):
        i+=1
        s+=l[i][j]

    else:
        j+=1
        s+=l[i][j]
    
if(i+2==n):
    
    if(l[i+1][j]>=l[i][j+1]):
        i+=1
        s+=l[i][j]
else:
    while(j<=n-1):
        
        s+=l[i][j]
        j+=1
if(j+2==n):
    
    if(l[i][j+1]>=l[i+1][j]):
        j+=1
        s+=l[i][j]
else:
    while(i<=n-1):
        
        s+=l[i][j]
        i+=1
print(s)