c=0

while(c!=4):
	cont=0
	c=0
	l=[]
	r=[]
	a=1000
	s=int(input(""))
	print(s)
	for i in range(0,3):
		q=s%10
		w=a%10
		s=int(s/10)
		a=int(a/10)
		print(s,a) 
		if(q==w):
			c=c+1
		else:
			l.append(q)
			r.append(w)
		print(c)
	for k in range(0,len(l)):
		for h in range(0,k):
			if(l[k]==r[h]):
				cont=cont+1
	print('bull=',cont)
	print("crow",c)
