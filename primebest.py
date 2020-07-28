import math
n=int(input(''))
arr=[0 for _ in range(n)]
for i in range(2,int(math.sqrt(n))+1):
    for j in range(2,int(n/i)):
        if(i*j<n):
            arr[int(i*j)]=1 
l=[]
for i in range(len(arr)):
    if(arr[i]==0):
        l.append(i)
c=0
tc=0

for i in range(2,len(l)):
    c+=l[i]

    if(c in l):
        tc+=1
        print(c)
print(tc-1)