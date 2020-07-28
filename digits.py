n=int(input(""))
c=0
for i in range(n):
    l=[int(d) for d in str(i)]
    l.sort()
    s=''.join(str(x) for x in l)
    
    if(i==int(s)):
        c+=1
    
print(c)



