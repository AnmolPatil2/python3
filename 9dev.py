n=input("enter the number")
i=1
l=list()
while(len(l)<int(n)):
    li=list(str(i))
    #print(li)
    while '9' in li:
        i=i+1
        li=list(str(i))
    
    l.append(i)
    print(i)
    i=i+1
print("nth term",l[-1])