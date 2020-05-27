n=int(input(""))

d=int(input(""))
temp=[]
a=int(input("").split(" "))
d=(n-d)%n
for i in range(len(a),0,-1):
	if(d==0):
		d=n
	temp[d]=a[i]
	d=d-1
print(temp)

