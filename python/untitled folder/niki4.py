a=input("")
l=[]
l=a.split()
z=[]
c=0
for i in range(0,len(l)):
	x=l[i]
	for k in range(0,len(x)):
		z.append(x[k])
	for m in range(0,len(z)):
		if(z[m]==z[-1-m]):
			c=c+1
if(c==len(z)):
	print("y")		
print(z)
