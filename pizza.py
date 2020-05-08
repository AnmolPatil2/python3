with open("e.in", "r") as file: 
    
    mn = file.readlines()
    print(mn)
    mn1=mn[0]
    l=mn[1]
    
    mn1=mn1.split()
    l=[int(x) for x in l.split()]
    print(l)

    m = int(mn1[0])
    n = int(mn1[1])

    
    
file.close()

co=0
o=[]


l.sort(reverse=True)
for y in range(0,len(l)):
	if(m-l[y]>0):
		m=m-l[y]
		print(m)
		co+=1
		o.append((n-1)-y)
o=o[::-1]
print(o)

file = open('e_example.txt','w') 
file.write(str(co)+"\n") 
file.write(" ".join([str(elem) for elem in o])) 
file.close() 