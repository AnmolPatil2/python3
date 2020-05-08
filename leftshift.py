a=(input(""))
a=a.split(" ")
temp=[]
n=(int(a[0]))
d=(int(a[1]))
for i in range(0,n):
	temp.append(0)

a=[int(i) for i in (input("").split(" "))]

d=(n-d-1)%n
for i in range(len(a)-1,-1,-1):
	if(d==0):
		temp[d]=a[i]
		d=n-1
	else:
		
		temp[d]=a[i]
		d=d-1
for i in range(n):
	print(temp[i],end=" ")

