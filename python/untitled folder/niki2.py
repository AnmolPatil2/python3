n=input("")
a=[]
a=n.split()
g=a[0]
for i in range(1,len(a)):
	if(len(g)<len(a[i])):
		g=a[i]
for j in range(0,len(a)):
	if(len(g)==len(a[j])):
		print(a[j],len(a[j]))
for i in range(1,len(a)):
	if(len(g)>len(a[i])):
		g=a[i]
for j in range(0,len(a)):
	if(len(g)==len(a[j])):
		print(a[j],len(a[j]))