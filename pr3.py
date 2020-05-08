n=int(input(""))

total=0
for t in range(2,int(n/2)+2):
	d=n
	c=0
	x=t

	
	while(d-x>0):
		if(x<=0 or d<=0):
			break
		
		
		if(d%2==0):
			
			if(d-x-1<=0):
				
				d=d-1
				
			else:
				d=d-1
				c=c+1
				#print(d+1,x)
				
		else:
			d=d-1
			c=c+1
			#print(d+1,x)
		if(d-x==0):
			x=x-2
			d=n
			
	
	
	total=total+c*t
	#print(total)
print(total+n)