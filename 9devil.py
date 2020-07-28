n=int(input("enter the number"))
j=0
for i in range(n):
    x=[f for f in str(i)]
    while(max(x)=="9" or j):
        j+=1 
    j+=1
print(j)
print(n+j)