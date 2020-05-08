a=int(input(""))
s=[]
d=[]
count=0
s=input("").split(" ")
	
max=s.max()
for i in range (0,max):
	d.append(0)

for i in range (0,len(s)):
	i=s[i]
	if(d[i]==0):
		d[i]=1
	if(d[i]==1):
		d[i]=0
		count=count+1
print(count)






	