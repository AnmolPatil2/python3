ac=[int(x) for x in (input("").split(" "))]
ex=[int(x) for x in (input("").split(" "))]
if(ac[2]!=ex[2]):
    if(ac[2]>ex[2]):
    	print(1000)
    	exit()
    else:
    	print(0)
    	exit()

elif(ac[1]!=ex[1]):
    if(ac[1]>ex[1]):
    	print((ac[1]-ex[1])*500)
    	exit()
    else:
    	print(0)
    	exit()

else:
    print(15*(ac[0]-ex[0]))