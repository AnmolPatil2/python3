t=int(input(""))
for _ in range(t):
   
    s,k1=[x for x in (input("").split(" "))]
    k=int(k1)
    k1=int(k1)
    
    i=k
    st=s[0:k]
    
    k+=k1
    c=0
    
    while(k<len(s)):
        
        st=st+"-"+"".join(s[i:k])
        c=c+1
        i=k
        k+=k1
        if(k>len(s)):
            
            a=k-k1
            if(a-1==len(s)):
                k=k-k1-1
            else:
                k1=c+3

    if(k1>c+1):
        
        print(-1)

    else:
        print(st)