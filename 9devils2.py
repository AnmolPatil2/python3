t=int(input(""))
for _ in range(t):
    
    
    l=[int(x) for x in (input(""))]
    l.reverse()
    pc=0
    for i in range(len(l)):
        if(i!=len(l)-1):
            t=0
            mp=i-1
            if(l[i]==9):
                pc+=(10**mp)*1 if i!=0 else 1
                t=1
                continue
            v=l[i]+pc 
            
            if(t==1 and v>9):
                pc+=2*(10**mp)*1  if i!=0 else 1
                continue
            
            





    

