import sys

a=list(input())
a.sort()
alen=len(a)
i=0
j=0
k=0
f=0
s=[]
for _ in range(0,alen):
	s.append(0)

while(i<alen and j<alen):
	if(a[i]==a[j]):

		j+=1
		s[k]+=1
		
	else:
		print(a[i],a[j])
		
		i=j

		k+=1
print(s)
k=0
su=0
for k in range(0,len(s)):
	if(s[k]==0):
		break
	su+=s[k]
print(k)
s=s[0:k]

print(s)
if(len(s)==1):
	print("y")
	sys.exit()
if(s[0]!=s[1]):
	print(s[1])
	if(s[0]>s[1]):
		if(su==s[0]*len(s) or su==s[0]*len(s)-1):
			print("y")
		else:
			print("n0")
	else:
		if(su==s[1]*len(s) or su==s[1]*len(s)-1):
			print("y")
		else:
			print("n1")
else:
	print(su)
	if(su==s[0]*len(s) or su==s[0]*len(s)-1):
		print("y")
	else:
		print(s[0]*len(s))





		