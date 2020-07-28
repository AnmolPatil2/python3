n=input("").split(" ")
di={}
for i in n:
    di[i]=n.count(i)

x=[x for x in di.values()]
x.sort(reverse=True)
x=x[2]
for k,j in di.items():
    if(j==x):
        print(k)
