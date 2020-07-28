str=input("")
i=1
n=len(str)
while(i<int(n/2)+1):
    j=n-i
    print(str[:i])
    if(str[:i]==str[j:n]):
        sr=str[:i]
        print(str[j:n])
        print(str.count(sr))
        
    i+=1