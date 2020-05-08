
i=0
count=0
t=0
f=0
while(i<n):
	if(t==0):
		
		if(f==1):
			count+=1

		if(s[i]=="U"):
			t=t+1
			

			f=0
			
			i+=1
		else:
			t=t-1
			
			f=1

			
			i+=1
	else:
		if(s[i]=="U"):
			t=t+1
			print(t)
			i+=1
		else:
			t=t-1
			
			i+=1

if(t==0):
	if(f==1):
		count+=1

