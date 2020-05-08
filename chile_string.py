a=input("")
b=input("")
a=list(a)
b=list(b)
maxy=0
alen=len(a)
blen=len(b)
arr=[[0 for _ in range(0,alen+1)] for j in range(0,blen+1)]

for x in range(0,alen):
	for y in range(0,blen):
		if(a[x]==b[y]):

			arr[x+1][y+1]=arr[x][y]+1
			if(arr[x+1][y+1]>maxy):
				maxy=arr[x+1][y+1]
			
		else:
			
			arr[x+1][y+1]=arr[x][y]

print(maxy)