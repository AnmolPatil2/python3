import math
n=int(input(""))
for i in range(0,n):
	a=int(input(""))
	st=list(input(""))
	
	count=0
	for q in range(0,a):
		if(st[q]=='1'):
			count=count+1
	#print(count)
	if(count==1):
		print(0)
	else:
		print(int(math.factorial(count)/((math.factorial(count-2))*2)))