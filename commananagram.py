
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    cc=0
    di={}
    for i in a:
        di[i]=a.count(i)
    for j in b:
        if(j in di.keys()):
            if(di[j]>0):
                di[j]-=1
                cc+=1
    
    return len(a)+len(b)-2*cc
    
 
if __name__ == '__main__':
    

   

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)
