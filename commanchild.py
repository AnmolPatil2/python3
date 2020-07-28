
# Complete the commonChild function below.
def commonChild(s1, s2):
    s3=set(s1)
    s4=set(s2)
    l1=[]
    ma=0
    l2=[]
    c=s3.intersection(s4)
    for i in s1:
        if(i in c):
            l1.append(i)
    for i in s2:
        if(i in c):
            l2.append(i)
    a=l1
    b=l2
    maxy=0
    alen=len(a)
    blen=len(b)
    arr=[[0 for _ in range(0,alen+1)] for j in range(0,blen+1)]

    for x in range(0,alen):
        for y in range(0,blen):
            if(a[x]==b[y]):

                arr[x+1][y+1]=arr[x][y]+1
                if(arr[x+1][y+1]>maxy):
                    maxy=arr[x+1][y+1]
                
            else:
                
                arr[x+1][y+1]=arr[x][y]
    print(arr)
    return maxy
                
                
                

 

if __name__ == '__main__':
    

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)
