h1=int(input(""))
h2=int(input(""))
b1=int(input(""))
b2=int(input(""))
t=0
for i2 in range(h1,h2+1):
    for j2 in range(b1, b2+1):
        i=i2
        j=j2
        while(j>0 and i>0):

            if(i==j):
                t+=1
                i=0
            elif(i==1):
                t=t+(i*j)
                i=-1
            elif(j==1):
                t=t+(i*j)
                j-=1
            elif(i>j):
                i=i-j
                t+=1
            else:
                j=j-i
                t+=1  
print(t) 

