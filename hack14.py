n=int(input(""))
l=[]

count=0

for k in range(0,n):

			
	q=[]
	o=input("")

	o = o.split(" ")

	a=(int(o[0]))
	q.append(a)
	
	b=(int(o[1]))
	i=2

	while(len(q)>0):
		
		for j in range(0,len(q)):
			r=q[j]%i
			i=i+1
			
			
			if(i>max(q)):
				print(-1)
				q=[]
				

				break
			
			
			if(r==b):
				count=count+1
				print(count)
				q=[]
				

				break
				
			else:
				if(len(q)==0):
					print(-1)

				if(r==0):
					continue

				else:
					if((r==1)):
						continue
					else:

						if(r in q):
							continue
						else:
							
							q.append(r)
							
							
			
			count=count+1
			i=2





	

		
		