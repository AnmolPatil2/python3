import math
n=int(input("number"))
ans=0
l=n+2
i=2
for x in range(4,l):
	
	while(1):

		if(x-i-2>=0):
			
			ans=math.factorial(x-i)/(2*math.factorial(x-i-2))+ans
			
			i=i+2
		else:
			i=2
			break
print(ans)