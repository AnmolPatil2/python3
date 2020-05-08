while(1):
	try:
		n=list(input(""))
	except:
		exit()
	
	if(len(n)==0):

		exit()
	flag=0

	for x in range(0,len(n)-1):
		
		if(n[x]=='/' and n[x-1]=='/'):
			flag=1
			e=''.join(n)
			print(e)
			continue
		
		if(n[x]=='>' and flag==0):
			if(n[x-1]=='-'):
				n[x-1]='.'
				del(n[x])
				n.append("")
				
				
	e=''.join(n)
	print(e)
	
	


