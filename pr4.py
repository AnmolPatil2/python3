a=999
b=998
c=997
for i in range(1,999):
	w=a*b*c
	d=[]
	w=list(str(w))
	
	d=w[::-1]
	d=''.join(d)
	w=''.join(w)
	if(w==d):
		print(w)
		
	else:
		a=a-1
		b=b-1
		c=c-1

	
	