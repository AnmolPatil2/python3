a=list(input())
b=list(input())
i=0
j=0
dell=0
alen=len(a)
blen=len(b)
a.sort()
b.sort()
while(i<alen and j<blen):
	if(a[i]==b[j]):
		i+=1
		j+=1
	else:
		if(a[i]<b[j]):
			dell+=1
			i+=1
		else:
			dell+=1
			j+=1
if(i!=alen):
	dell=dell+(alen-i)
if(j!=blen):
	dell=dell+(blen-j)

print(dell)
