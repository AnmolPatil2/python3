n=int(input(""))
for i in range(0,n):
	a=[]
	a=((input("").split(" ")))
	t=int(a[0])
	b=[]
	k=int(a[1])
	a=input("").split(" ")
	for x in range(0,t):
		b.append(a[x])
	b.sort()	
	b=b[0:k]
	
	s=len(b)
	d=set(b)
	print(1)