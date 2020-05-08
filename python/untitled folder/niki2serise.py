c=0
for i in range(2,100):
	for j in range(2,i):
		if((i%j)!=0):
			c=c+1
		
		
		if(c==(i-2)):
			print(i)