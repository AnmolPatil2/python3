import operator
books,lib,dayS=[int(x) for x in (input("").split())]
score=[int(x) for x in (input("").split())]
l11=[x for x in range(len(score))]
score=dict(zip(l11, score)) 
di={}
for i in range(lib):
    
    x=[]
    no_books,sign_up,ship=[int(x) for x in (input("").split())]
    l=[int(x) for x in (input("").split())]
    for k,v in score.items():
        if(k in l):
            x.append(k)
    x.sort(reverse=True)
    di[i]=[no_books,sign_up,ship,x]
tt={}

for i in range(lib):
    t=int(di[i][0]/di[i][2])+1
    tt[t]=i
tt=dict(sorted(tt.items()))
print(tt)
totalD=0
startD=0

file = open('x3.txt','w') 
for i,k in tt.items():
    startD+=di[k][1]
    totalD+=startD+(int(di[k][0]/di[k][2])+1)

    if(totalD>dayS):
        d=dayS-startD

        bs=d*di[k][2]
        
        di[k][3]=di[k][3][0:bs]
        di[k][0]=bs
    

        


        
        break
file.write(str(k+1)+"\n") 

#print(di[0][3])
#di[1][0]=di[1][0]-1
#di[0][3]=di[0][3][::-1]
for i,k in tt.items():
    file.write(str(k)+" "+str(di[k][0])+"\n") 
    
    for z in (di[k][3]):
        file.write(str(z)+" ") 
    file.write("\n") 
     
file.close()


    



    


