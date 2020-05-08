n=int(input(""))
l=[]
count=0
for k in range(0,n):
	k=input("")
	k = k.split(" ")
	for f in range(0,2):

		l.append(int(k[f]))
		
i=0
d=len(l)-3
while (i<len(l)):
	j=i
	while(j<d):
		if(l[j]<=l[j+2]):
			
			if(l[j+1]<=l[j+3]):
				count=count+1
		j=j+2
	i=i+2
print(count)

