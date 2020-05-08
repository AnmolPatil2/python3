with open("a.in", "r") as file: 
    
    mn = file.readlines()
    print(mn)
    mn1=mn[0]
    l=mn[1]
    
    mn1=mn1.split()
    l=l.split()
    print(l)

    m = int(mn1[0])
    n = int(mn1[1])
    print(m,n)
    
file.close()
