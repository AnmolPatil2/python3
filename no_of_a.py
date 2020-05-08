s=input("")
n=int(input(""))
l=s.length()
ain=0
count=0
p=n/l
tc=n%l
for i in range(0,int(tc)):
	if("a"==s[i]):
		count+=1
s.sort()
for i in s:
	if(i=="a"):
		ain+=1
count=count+(ain*p)
return(count)