n=int(input(""))
l=[]
d=[]
q=2
c=0
while(q>=2):
    q=int(n/2)
    print(q)
    
    r=(n%2)
    n=q
    print(r)
    l.append(r)
l.append(q)
for s in l:
	print(s)
	if(s==1):
		c=c+1
	else:
		d.append(c)
		c=0
print(d)