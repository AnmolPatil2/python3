import math
n=int(input(''))
arr=[0 for _ in range(n)]
for i in range(2,int(math.sqrt(n))+1):
    for j in range(2,int(n/i)):
        if(i*j<n):
            arr[int(i*j)]=1 

c=0
tc=0
i=2
while(tc<n):
    if(arr[i]==0):
        tc+=i
        
        if(tc<n):
            if(arr[tc]==0):
                c+=1
    i+=1
print(c-1)