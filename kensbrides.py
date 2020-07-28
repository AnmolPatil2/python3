def countfor(s,c):
    i=0
    while(c>0):
        print(b[i])
        if(b[i]==s):
            c-=1
        i+=1
    return i-1
    
n=int(input(""))
b,g=input("").split(' ')
gr=g.count("r")
gm=g.count("m")
br=b.count("r")
bm=b.count("m")
if(br-gr==0):
    print('0')
elif(br-gr>0):
    ans=n-countfor("r",gr+1)
else:
    ans=n-countfor("m",gm+1)
print(ans)
