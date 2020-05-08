s=input("")
di={}
for x in s:

    di[x]=s.count(x)
l=[]
for i,v in di.items():
    if(v>1):
        l.append(i)

box=[]
s=list(s)
print(s)
f=[]
f1=0
for x in range(len(s)):
    t=x+1
    print(str(t)+"t")
    
    if(s[x] in l):
        print(s[x])
        j=0
        while(j+x+1<(len(s))):
            
            if(s[x] == s[x+j+1] or s[x]==s[len(s)-j-1]):
                t+=j
                f.append(t)
                s[x]=0
                f1=1
                
                
            j+=1
if(f1==0):
    print("Tie")
    exit(0)
e=(min(f))
print(f)
if(e%2==0):
    print("Alice")
else:
    print("Bob")


