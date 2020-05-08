
f=0
l=["rock","paper","ses"]
p1=0
p2=0
while(f==0):
	i=input("")
	s=input("")
	if(i != l):
		print("invalid")
	if(s!=l):
		print("invalid")
	if(i=="rock"):
		if(s=="paper"):
			print("2 wins")
			p2=p2+1
		elif(s=="ses"):
			print("1 wins")
			p1=p1+1
		elif(i==s):
			print("draw")
	elif(i=="paper"):
		if(s=="rock"):
			print("1 wins")
			p1=p1+1
		elif(s=="ses"):
			print("2 wins")
			p2=p2+1
		elif(i==s):
			print("draw")
	elif(i=="ses"):
		if(s=="rock"):
			print("2 wins")
			p2=p2+1
		elif(s=="paper"):
			print("1 wins")
			p1=p1+1
		elif(i==s):
			print("draw")
	d=input("try again y or n")
	if(d=="n"):
		f=2
print("player1=",p1,"player2=",p2)
if(p1>p2):
	print("p1 wins")
else:
	print("p2 wins")
if(p1==p2):
	print("draw game")
