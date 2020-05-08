a=int(input(""))
l1=[]
l2=[]
l3=[]
letter=[]
p=0
final=[]
o=0
for i in range(0,a):
    q=input("")
    
    l1=q.split()
    
    for j in range(0,len(l1)):
        if(l1[j].isdigit()):
            l2.append(l1[j])
            l3.append(j)
        else:
            letter.append(l1[j])
    l2.sort()
    letter.sort()
    for k in range(0,len(l1)):
        if(k in l3):
            final.append(l2[p])
            p=p+1
        else:
            final.append(letter[o])
            o=o+1
            
for t in range(len(l1)):        
    print(final[t])   